from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

import json


with open("secret.json") as s:
    SECRET = json.load(s)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)
    price = db.Column(db.Integer, unique=False)
    country = db.Column(db.String(20), unique=False)
    weight = db.Column(db.String(20), unique=False)
    height = db.Column(db.String(20), unique=False)

    def __init__(self, name: str = "", price: int = 0, country: str = "",
                 weight: int = 0, height: int = 0):
        self.name = name
        self.price = price
        self.country = country
        self.weight = weight
        self.height = height


class DeviceSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'price', 'country', 'weight', 'height')


device_schema = DeviceSchema()
device_schemas = DeviceSchema(many=True)


# endpoint to create new user
@app.route("/device", methods=["POST"])
def add_device():
    try:
        info_about_class = DeviceSchema().load((request.json))
        device = Device(**info_about_class)
        db.session.add(device)
        db.session.commit()
        return device_schema.jsonify(device)
    except ValidationError:
        abort(400)



# endpoint to show all users
@app.route("/device", methods=["GET"])
def get_user():
    all_users = Device.query.all()
    result = device_schemas.dump(all_users)
    return jsonify({'user_schema': result})


# endpoint to get user detail by id
@app.route("/device/<id>", methods=["GET"])
def user_detail(id):
    user = Device.query.get(id)
    if not user:
        abort(404)
    return device_schema.jsonify(user)


# endpoint to update user
@app.route("/device/<id>", methods=["PUT"])
def user_update(id):
    device = Device.query.get(id)
    if not device:
        abort(404)

    device.name = request.json['name']
    device.price = request.json['price']
    device.country = request.json['country']
    device.weight = request.json['weight']
    device.height = request.json['height']

    db.session.commit()
    return device_schema.jsonify(device)


# endpoint to delete user
@app.route("/device/<id>", methods=["DELETE"])
def user_delete(id):
    device = Device.query.get(id)
    if not device:
        abort(404)
    db.session.delete(device)
    db.session.commit()

    return device_schema.jsonify(device)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
