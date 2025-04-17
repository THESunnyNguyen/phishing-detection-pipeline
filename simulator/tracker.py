from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/click", methods=["GET"])
def track():
    with open("clicks.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - Clicked from {request.remote_addr}\n")
    return "Tracked", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)