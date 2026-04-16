from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import subprocess
import json

PORT = 1515

def find_formable_words(letters):
    # equivalente ao subprocess_t
    process = subprocess.Popen(
        ["python3", "scrabble_word_finder.py", letters],
        stdout=subprocess.PIPE,
        text=True
    )

    words = []

    # equivalente ao getline
    for line in process.stdout:
        words.append(line.strip())

    process.wait()  # equivalente ao waitpid

    return words


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse.urlparse(self.path)

        if parsed.path == "/words":
            query = urlparse.parse_qs(parsed.query)

            if "letters" in query:
                letters = query["letters"][0]
                letters = "".join(sorted(letters))

                words = find_formable_words(letters)

                payload = {
                    "possibilities": words
                }

                response = json.dumps(payload)

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(response)))
                self.end_headers()

                self.wfile.write(response.encode())

        elif parsed.path == "/" or parsed.path == "/index.html":
            with open("index.html", "r") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()

            self.wfile.write(content.encode())

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), MyHandler)
    print(f"Servidor rodando em http://localhost:{PORT}")
    server.serve_forever()
