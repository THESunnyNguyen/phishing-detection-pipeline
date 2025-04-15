from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    email_body = request.json.get('body', '')
    if "reset password" in email_body.lower():
        return jsonify({"phishing": True})
    return jsonify({"phishing": False})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000)
