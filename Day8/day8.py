from flask import Flask, request

from products import products

app = Flask(__name__)

@app.route('/getdata', methods = ['GET'])
def get_data():
    return "<h1>Hello World</h1>"

@app.route("/", methods = ['GET'])
def home():
    return "<h1>welcome to the home page</h1>"

@app.route('/getdata/<name>/<age>', methods = ['GET'])
def get_data_name(name, age):
    return f"<h1>Hello {name}, you are {age} years old</h1>"


@app.route('/products/<int:id>', methods = ['GET'])
def get_id_product(id):
    for product in products:
        if product["id"] == id:
            return f"""
                <h1>id: {product["id"]}
                <h1>name: {product["name"]}
                <h1>category: {product["category"]}
                <h1>price: {product["price"]}
                <h1>stock: {product["stock"]}
                <h1>rating: {product["rating"]}
                <h1>is_available: {product["is_available"]}
                """

@app.route("/products", methods=['GET'])
def get_products():
    producthtml = ""
    for product in products:
        producthtml += f"""
            <h1>id: {product["id"]}
            <h1>name: {product["name"]}
            <h1>category: {product["category"]}
            <h1>price: {product["price"]}
            <h1>stock: {product["stock"]}
            <h1>rating: {product["rating"]}
            <h1>is_available: {product["is_available"]}
            """
        return producthtml


print(products)

if __name__ == '__main__':
    app.run(debug=True)
print("Hello World")