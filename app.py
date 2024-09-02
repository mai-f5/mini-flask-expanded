from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

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


class GetUsersSchema(Schema):
    organization = fields.Integer(required=True)


class UpdateUsersSchema(Schema):
    organization = fields.String(required=True)
    users = fields.List(fields.String)


# Initialize schema instances
user_schema = UserSchema()
product_schema = ProductSchema()
order_schema = OrderSchema()
comment_schema = CommentSchema()
login_schema = LoginSchema()
search_schema = SearchSchema()
users_get_schema = GetUsersSchema()
users__post_schema = UpdateUsersSchema()


@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    try:
        validated_data = user_schema.load(data)  # Validate and deserialize input
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Process user creation with validated_data
    return jsonify({"message": "User created successfully", "data": validated_data}), 201


@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    try:
        validated_data = product_schema.load(data)  # Validate and deserialize input
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Process product creation with validated_data
    return jsonify({"message": "Product created successfully", "data": validated_data}), 201


@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    try:
        validated_data = order_schema.load(data)  # Validate and deserialize input
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Process order creation with validated_data
    return jsonify({"message": "Order created successfully", "data": validated_data}), 201


@app.route('/comment', methods=['POST'])
def create_comment():
    data = request.json
    try:
        validated_data = comment_schema.load(data)  # Validate and deserialize input
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Process comment creation with validated_data
    return jsonify({"message": "Comment created successfully", "data": validated_data}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        validated_data = login_schema.load(data)  # Validate and deserialize input
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Process login with validated_data
    return jsonify({"message": "Login successful", "data": validated_data}), 200


@app.route('/users/<organization>', methods=['GET', 'POST'])
def users(organization):
    if request.method == 'GET':
        params = {"organization": organization}
        try:
            # Validate the organization parameter
            validated_data = users_get_schema.load(params)
        except ValidationError as err:
            return jsonify(err.messages), 400  # Return validation errors

        # Process search with validated_data
        return jsonify({"message": "Users for org results", "data": validated_data}), 200

    elif request.method == 'POST':
        # Handle the POST request (assuming it expects JSON data)
        data = request.json
        # Here you might want to validate the incoming JSON data with another schema
        # Assuming you have some schema like user_schema for POST request validation

        try:
            validated_data = users__post_schema.load(data)  # Validate and deserialize input
        except ValidationError as err:
            return jsonify(err.messages), 400  # Return validation errors

        # Process user creation or any other operation with the validated data
        return jsonify({"message": "Success", "data": validated_data}), 200


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    try:
        validated_data = search_schema.load(data)  # Validate and deserialize input
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Process search with validated_data
    return jsonify({"message": "Search results", "data": validated_data}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)