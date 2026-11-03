from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/orders")
def orders():
    return jsonify([
        {"id": 1001, "user_id": 1, "product_id": 101},
        {"id": 1002, "user_id": 2, "product_id": 102}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
