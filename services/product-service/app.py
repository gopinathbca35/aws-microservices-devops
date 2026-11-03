from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/products")
def products():
    return jsonify([
        {"id": 101, "name": "Laptop", "price": 55000},
        {"id": 102, "name": "Mobile", "price": 25000}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
