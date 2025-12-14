from flask import Flask, request, jsonify

# 1️⃣ Create the Flask app FIRST
app = Flask(__name__)

# 2️⃣ Temporary in-memory storage
notes = []


# 3️⃣ Routes come AFTER app is defined
@app.route("/")
def home():
    return "Notes API is running"


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Text is required"}), 400

    note = {
        "id": len(notes) + 1,
        "text": data["text"]
    }

    notes.append(note)
    return jsonify(note), 201


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)


# 4️⃣ Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
