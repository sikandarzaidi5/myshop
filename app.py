from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id":1, "title":"Classic Sneakers", "price":"Rs 6,499", "image":"static/images/product1.jpg"},
    {"id":2, "title":"Leather Wallet",   "price":"Rs 1,299", "image":"static/images/product2.jpg"},
    {"id":3, "title":"Wireless Earbuds", "price":"Rs 3,899", "image":"static/images/product3.jpg"},
]

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)

@app.route("/api/products")
def products_api():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
