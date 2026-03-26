from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return send_from_directory(BASE, "index.html")

@app.route("/style.css")
def style():
    return send_from_directory(BASE, "style.css")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)
    if not data or "message" not in data:
        return jsonify({"error": "missing message"}), 400

    text = data["message"].strip().lower()
    if not text:
        return jsonify({"response": "Please type something."})
    if "hello" in text or "hi" in text:
        reply = "Hello! How can I help?"
    elif "study" in text:
        reply = "Study tip: take breaks and explain ideas aloud."
    elif "how are you" in text:
        reply = "I am good, thank you!" //"what about you?"
    elif "bye" in text or "goodbye" in text:
        reply = "Bye! Talk soon."
    else:
        reply = "Sorry, I don't know that yet."
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)