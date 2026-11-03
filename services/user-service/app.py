from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Gopinath"},
        {"id": 2, "name": "DevOps Engineer"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
