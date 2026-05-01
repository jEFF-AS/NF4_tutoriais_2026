import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister


from flask import request
from flask_jwt_extended import create_access_token
from models.user import UserModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["JWT_SECRET_KEY"] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.environ.get('SECRET_KEY')
api = Api(app)


api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


jwt = JWTManager(app)
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return {"message": "Missing JSON"}, 400

    user = UserModel.find_by_username(data.get("username"))

    if user and user.check_password(data.get("password")):
        token = create_access_token(identity=user.id)
        return {"access_token": token}, 200

    return {"message": "Invalid credentials"}, 401

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=False)
