from flask import Flask, request, jsonify
from marshmallow import Schema, fields

app = Flask(__name__)


class UserSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)


class ProductSchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)


class OrderSchema(Schema):
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)


class CommentSchema(Schema):
    post_id = fields.Integer(required=True)
    content = fields.String(required=True)


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class SearchSchema(Schema):
    query = fields.String(required=True)
    category = fields.String(required=False)


@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    # Process user creation
    return jsonify({"message": "User created successfully", "data": data}), 201


@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    # Process product creation
    return jsonify({"message": "Product created successfully", "data": data}), 201


@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    # Process order creation
    return jsonify({"message": "Order created successfully", "data": data}), 201


@app.route('/comment', methods=['POST'])
def create_comment():
    data = request.json
    # Process comment creation
    return jsonify({"message": "Comment created successfully", "data": data}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Process login
    return jsonify({"message": "Login successful", "data": data}), 200


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    # Process search
    return jsonify({"message": "Search results", "data": data}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)