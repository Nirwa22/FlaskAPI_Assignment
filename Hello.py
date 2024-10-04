from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import uuid
import json

load_dotenv()
API_KEY = os.getenv("SECRET_API_KEY")
app = Flask(__name__)
CORS(app)

with open("users.json", "r") as json_file:
    new_users = json.load(json_file)


@app.route("/")
def home():
    return "Home Route"


@app.route("/Users_Information")
def user_information():
    return new_users


@app.route("/Authorization", methods=['POST'])
def authorize_user():
    data = request.get_json()
    new_data = {"Name": data['Name'], "Age": data["Age"], "Gender": data["Gender"]}
    api = request.headers.get("Authorization")
    if api and api != API_KEY:
        return "Unauthorized access"
    elif not api:
        return "API KEY needed"
    elif api == API_KEY:
        session_id = str(uuid.uuid4())
        new_data["id"] = session_id
        new_list = list(new_users)
        new_list.append(new_data)
        with open("users.json", "w") as json_new_file:
            json.dump(new_list, json_new_file, indent=4)
        return f"Authorization Successful : Your Session_id is {session_id}"


@app.route("/Get_User_Information", methods=["POST"])
def get_user_data():
    api = request.headers.get("Authorization")
    user_id = request.get_json()
    if api and api != API_KEY:
        return "Unauthorized access"
    elif not api:
        return "API Key needed"
    elif api == API_KEY:
        with open("users.json", "r") as new_file:
            users = json.load(new_file)
        for i in users:
            if i["id"] == user_id["id"]:
                return {"Name": i["Name"], "Age": i["Age"], "Gender": i["Gender"]}
                break
        return "Session_id does not exist"


if __name__ == "__main__":
    app.run(debug=True)


