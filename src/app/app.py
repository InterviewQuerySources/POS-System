from flask import Flask, render_template, request

import sql

# Instantiating global variables
# the db_driver is a sql driver wrapper class
# visit src/app/sql.py for more details.
app: Flask = Flask(__name__)
db_driver = sql.driver()


# Here, we render our index.html
@app.route('/')
def index():
    return render_template('index.html')


# This is the endpoint where we accept POST requests from the order form in our index.html
@app.route('/submit_order', methods=['POST'])
def order_now():
    name = request.form.get('customerName')
    items = request.form.getlist('item')

    # Execute the query using the database driver
    try:
        # Insert the order first
        order_query = f"INSERT INTO orders (customer_name) VALUES ('{name}')"
        db_driver.execute(order_query)

        # Get the order ID
        id_query = "SELECT LAST_INSERT_ID() FROM orders"
        id = db_driver.fetch(id_query)[0]['LAST_INSERT_ID()']
        print(id)

        # For all items ordered, we insert them as orders in the database
        for item_name in items:
            # Get the item_id for the current item_name from the database
            item_query = f"SELECT itemID FROM items WHERE item_name = '{item_name}'"

            item_id = db_driver.fetch(item_query)[0].get('itemID')
            # Insert the order into the database using the item_id
            order_query = f"INSERT INTO order_items values({id}, {item_id})"
            db_driver.execute(order_query)

        return f"<h1>Order from {name} for items {', '.join(items)} has been submitted successfully</h1>"
    except Exception as e:
        return f"<h1>Error submitting order: {str(e)}</h1>"


# run our flask instance
if __name__ == "__main__":
    app.run()
