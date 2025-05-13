from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_product():
    product_info = {
        'name': 'Wireless Headphones',
        'brand': 'SoundMax',
        'price': 129.99,
        'features': [
            'Bluetooth 5.3',
            'Noise Cancellation',
            '20-hour Battery Life',
            'Built-in Microphone'
        ]
    }

    # Passing the entire dictionary as one object named 'product'
    return render_template('product.html', product=product_info)

if __name__ == '__main__':
    app.run(debug=True)
