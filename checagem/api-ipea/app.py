from flask import Flask

from controllers.health_controller import health
from controllers.serie_controller import serie

app = Flask(__name__)

# rotas
app.add_url_rule("/health", "health", health)
app.add_url_rule("/serie/<codigo>", "serie", serie)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
