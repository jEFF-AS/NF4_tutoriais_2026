from app import app
from db import db

db.init_app(app)

with app.app_context():
    db.create_all()

app.run(port=5000, debug=True)
