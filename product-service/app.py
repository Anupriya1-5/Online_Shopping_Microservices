from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Wireless Mouse", "price": 800},
    {"id": 3, "name": "Keyboard", "price": 1500},
    {"id": 4, "name": "Headphones", "price": 2500}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Product Service is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
