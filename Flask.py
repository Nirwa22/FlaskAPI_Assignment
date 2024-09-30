from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Home Route"


@app.route("/User_Information")
def user_data():
    user_data = [
                {"Name": "Sarah", "Age": 34, "Gender": "f"},
                {"Name": "Maha", "Age": 15, "Gender": "f"},
                {"Name": "Ali", "Age": 40, "Gender": "m"},
                {"Name": "Tahir", "Age": 63, "Gender": 'm'},
                {"Name": "Ayesha", "Age": 25, "Gender": "f"},
                {"Name": "Zahid", "Age": 23, "Gender": "m"},
             ]
    return jsonify(user_data)


if __name__ == "__main__":
    app.run(debug=True)


