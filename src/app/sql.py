import mysql.connector


# This class is a wrapper driver class for connecting to an SQL Server

class driver:
    # These are the default values for most SQL servers
    # modify as needed.
    def __init__(self,
                 host="localhost",
                 database="POS_IQ",
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
    def execute(self, query, params=None):
        """Execute a query that does not return a result set."""
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        cursor.close()

    def fetch(self, query, params=None):
        """Execute a query that returns a result set."""
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    # retrieves the connection instance from this
    # wrapper class.
    def get_connection(self):
        return self.conn

