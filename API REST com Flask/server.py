from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

def find_formable_words(letters):
    process = subprocess.Popen(
        ["python3", "scrabble_word_finder.py", letters],
        stdout=subprocess.PIPE,
        text=True
    )

    words = [line.strip() for line in process.stdout]

    process.wait()
    return words


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/words")
def words():
    letters = request.args.get("letters", "")

    letters = "".join(sorted(letters))

    words = find_formable_words(letters)

    return jsonify({
        "possibilities": words
    })


if __name__ == "__main__":
    app.run(port=1515, debug=True)
