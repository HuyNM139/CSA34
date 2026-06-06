from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Viết các API để trả về dữ liệu
@app.route("/", methods = ['GET'])
def home():
    return "<h1>hello world</h1>"
@app.route("/get_person_information", methods=["GET"])
def get_person_information():
    data = {
        "name": "Huy",
        "email": "qwertyuiop123@gmail.com",
        "phone": "0901548394",
        "favorites": ["football","basketball","swimming"]
    }
    
    data = jsonify(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)
print("Hello World")