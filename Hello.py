from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os, uuid

load_dotenv()
API_KEY = os.getenv("SECRET_API_KEY")
app = Flask(__name__)
CORS(app)

session_file = {}
users = [
                {"id": 1, "Name": "Sarah", "Age": 34, "Gender": "f"},
                {"id": 2, "Name": "Maha", "Age": 15, "Gender": "f"},
                {"id": 3, "Name": "Ali", "Age": 40, "Gender": "m"},
                {"id": 4, "Name": "Tahir", "Age": 63, "Gender": 'm'},
                {"id": 5, "Name": "Ayesha", "Age": 25, "Gender": "f"},
                {"id": 6, "Name": "Zahid", "Age": 23, "Gender": "m"},
             ]


@app.route("/home")
def home():
    return "Home Route"


@app.get("/Users_Information")
def user_information(data=users):
    return jsonify(data)


@app.route("/User_info", methods=['POST'])
def user_data2():
    data = request.get_json()
    new_data = {"Name": data['Name'], "Age": data["Age"], "Gender": data["Gender"]}
    return jsonify(new_data)


@app.route("/Authorization", methods=['POST'])
def authorize_user():
    data = request.get_json()
    new_data = {"Name": data['Name'], "Age": data["Age"], "Gender": data["Gender"]}
    api = request.headers.get("Authorization")
    if api and api != API_KEY:
        return "Unauthorized User"
    elif not api:
        return "API KEY needed"
    elif api == API_KEY:
        session_id = uuid.uuid4()
        new_data["session_id"] = session_id
        session_file.update(new_data)
        users.append(new_data)
        return f"Authorization Successful : Your Session_id is {session_id}"


if __name__ == "__main__":
    app.run(debug=True)


