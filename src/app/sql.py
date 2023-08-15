import mysql.connector


# This class is a wrapper driver class for connecting to an SQL Server

class driver:
    # These are the default values for most SQL servers
    # modify as needed.
    def __init__(self,
                 host="localhost",
                 database="food_project",
                 username="root",
                 password=""):
        self.conn = mysql.connector.connect(
            host=host,
            database=database,
            user=username,
            password=password
        )

    # To interact with the pyodbc result set,
    # make use of the iterators. Do the following
    #   rows = query("SELECT * FROM TBL")
    #   for row in rows:
    #       row['first_name']
    #       ... do operations here ...
    def query(self, query_string: str):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query_string)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    # retrieves the connection instance from this
    # wrapper class.
    def get_connection(self):
        return self.conn

    # overloaded destructor
    def __del__(self):
        if self.conn.is_connected():
            self.conn.close()
