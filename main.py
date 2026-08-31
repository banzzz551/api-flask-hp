from flask import Flask, jsonify, request

app = Flask(__name__)

db_users = [
    {"id": 1, "nama": "Budi", "role": "Backend Developer"},
    {"id": 2, "nama": "Siti", "role": "UI/UX Designer"}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "online", "message": "API Flask dari HP jalan!"})

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({"status": "success", "data": db_users})

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(db_users) + 1,
        "nama": data.get("nama"),
        "role": data.get("role")
    }
    db_users.append(new_user)
    return jsonify({"status": "success", "data": new_user}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
