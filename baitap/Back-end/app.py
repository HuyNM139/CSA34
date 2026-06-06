from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/", methods = ['GET'])
def home():
    return "<h1>hello world</h1>"

@app.route("/products", methods=['GET'])
def get_products():
    products = [
        {
            "id": 1,
            "name": "Wireless Mouse",
            "category": "Electronics",
            "price": 25.99,
            "stock": 120,
            "rating": 4.5,
            "is_available": True,
        },
        {
            "id": 2,
            "name": "Gaming Keyboard",
            "category": "Electronics",
            "price": 79.99,
            "stock": 45,
            "rating": 4.7,
            "is_available": True,
        },
        {
            "id": 3,
            "name": "Running Shoes",
            "category": "Fashion",
            "price": 59.50,
            "stock": 30,
            "rating": 4.3,
            "is_available": True,
        },
        {
            "id": 4,
            "name": "Coffee Mug",
            "category": "Home & Kitchen",
            "price": 12.99,
            "stock": 200,
            "rating": 4.1,
            "is_available": True,
        },
        {
            "id": 5,
            "name": "Office Chair",
            "category": "Furniture",
            "price": 149.99,
            "stock": 10,
            "rating": 4.6,
            "is_available": False,
        },
    ]
    
    products = jsonify(products)
    return products

@app.route("/products/<int:id>", methods=['GET'])
def get_product(id):
    products = [
        {
            "id": 1,
            "name": "Wireless Mouse",
            "category": "Electronics",
            "price": 25.99,
            "stock": 120,
            "rating": 4.5,
            "is_available": True,
        },
        {
            "id": 2,
            "name": "Gaming Keyboard",
            "category": "Electronics",
            "price": 79.99,
            "stock": 45,
            "rating": 4.7,
            "is_available": True,
        },
        {
            "id": 3,
            "name": "Running Shoes",
            "category": "Fashion",
            "price": 59.50,
            "stock": 30,
            "rating": 4.3,
            "is_available": True,
        },
        {
            "id": 4,
            "name": "Coffee Mug",
            "category": "Home & Kitchen",
            "price": 12.99,
            "stock": 200,
            "rating": 4.1,
            "is_available": True,
        },
        {
            "id": 5,
            "name": "Office Chair",
            "category": "Furniture",
            "price": 149.99,
            "stock": 10,
            "rating": 4.6,
            "is_available": False,
        },
    ]
    for product in products:
        if product["id"] == id:
            return jsonify(product)
        
if __name__ == '__main__':
    app.run(debug=True)
print("Hello World")