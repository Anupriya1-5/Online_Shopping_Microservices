from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Anu", "email": "anu@example.com"},
    {"id": 2, "name": "Rahul", "email": "rahul@example.com"},
    {"id": 3, "name": "Priya", "email": "priya@example.com"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "User Service is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
  
