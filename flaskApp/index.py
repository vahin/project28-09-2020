from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

data = [{"Timestamp":"2007 10 21 12:56:34", "Contact":"9876543210", "Name":"John", "done":False, "id":1},
{"Timestamp":"2019 12 23 12:23:54", "Contact":"0123456789", "Name":"Rahul", "done":False, "id":2}
]

@app.route("/add-data", methods=["POST"])
def add_data():
    now = datetime.now()
    now = now.strftime("%Y %m %d %H:%M:%S")
    if not request.json:
        return jsonify({"status":"ERR", "message":"Provide Data"}, 400)

    data.append({"Timestamp":now, "Contact":request.json["Contact"], "Name":request.json["Name"], "done":False, "id": data[-1]["id"] + 1})
    return jsonify({"status":"success", "message":"Data added with the info on "+now})

@app.route("/fetch-data", methods=["GET"])
def fetch_data():
    return jsonify({"data":data})

if (__name__ == "__main__"):
    app.run(debug=True)
