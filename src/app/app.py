from flask import Flask, render_template, request

import sql

app: Flask = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_order', methods=['POST'])
def order_now():
    name = request.form.get('customerName')
    items = request.form.getlist('item')
    return f"<h1>Received orders from {name} for items {items}</h1>"


if __name__ == "__main__":
    app.run()
