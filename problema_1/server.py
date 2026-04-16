from flask import Flask, jsonify
import random

app = Flask(__name__)

def payment_call():
    total_cost = 0
    steps = []

    while True:
        event = random.randint(1, 3)

        if event == 1:
            cost = 3
            steps.append(3)
            total_cost += cost
            break

        elif event == 2:
            cost = 5
            steps.append(5)
            total_cost += cost

        else:
            cost = 7
            steps.append(7)
            total_cost += cost

    return total_cost, steps


@app.route("/payment")
def payment():
    total_cost, steps = payment_call()

    return jsonify({
        "steps": steps,
        "expression": " + ".join(map(str, steps)),
        "total_cost": total_cost
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
