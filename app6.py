from flask import Flask, render_template, request

app = Flask(__name__)

# Example list of products categorized by type
PRODUCTS = {
    'electronics': ['Smartphone', 'Laptop', 'Headphones'],
    'fashion': ['T-shirt', 'Jeans', 'Jacket'],
    'groceries': ['Apple', 'Banana', 'Carrot'],
}

@app.route("/")
def filter_products():
    # Retrieve the 'category' GET parameter from the URL
    category = request.args.get("category")

    # Check if a valid category was provided, default to 'electronics'
    if not category or category.lower() not in PRODUCTS:
        category = 'electronics'

    # Fetch products based on category
    products = PRODUCTS[category.lower()]

    return render_template("shop.html", products=products, category=category)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
