import pip
import mysql.connector

# run this file first to install the required dependencies

dependency_list = ['mysql-connector-python', 'flask']


def main():
    print('Now retrieving project dependencies...')
    for dependency in dependency_list:
        print('Installing package:', dependency)
        pip.main(['install', dependency])
        print('Installed package:', dependency)
    print('Now creating the database')


    def create(
               host="localhost",
               database="",
               username="root",
               password=""):
        conn = mysql.connector.connect(
            host=host,
            database=database,
            user=username,
            password=password,
        )
        query = ["""
                -- Create the database if it doesn't exist
            CREATE DATABASE IF NOT EXISTS POS_IQ;
            """, "USE POS_IQ;", """-- Create the orders table
            CREATE TABLE IF NOT EXISTS orders (
                orderID INT AUTO_INCREMENT PRIMARY KEY,
                Customer_Name VARCHAR(255) NOT NULL
            );""", """
            -- Create the items table
            CREATE TABLE IF NOT EXISTS items (
                itemID INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(255) NOT NULL,
                UNIQUE (item_name)  -- Ensure no duplicate items by name
            );""", """
            -- Create the order_items junction table
            CREATE TABLE IF NOT EXISTS order_items (
                orderID INT,
                itemID INT,
                FOREIGN KEY (orderID) REFERENCES orders(orderID) ON DELETE CASCADE, 
                FOREIGN KEY (itemID) REFERENCES items(itemID) ON DELETE CASCADE,
                PRIMARY KEY (orderID, itemID)  -- Composite primary key
            );"""]


        cursor = conn.cursor(dictionary=True)
        for q in query:
            cursor.execute(q)
        items = ['Burger', 'Fried Chicken', 'Soda', 'Ice Cream']
        for item in items:
            print('inserting', item)
            cursor.execute(f"SELECT 1 FROM items WHERE item_name like '{item}'")
            result = cursor.fetchall()
            print(len(result))
            if len(result) is 0:
                query = f"INSERT INTO items values (null, '{item}');"
                print('inserting', query)
                cursor.execute(query)
        conn.commit()
        return


    create()


if __name__ == '__main__':
    main()
