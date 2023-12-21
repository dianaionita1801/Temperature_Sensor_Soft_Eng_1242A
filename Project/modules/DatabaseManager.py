import mysql.connector as sql

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
    
    # function to connect to the database
    def connect(self):
        try:
            self.conn = sql.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database.")
        except sql.Error as e:
            print(f"Error connecting to the database: {e}")
    
    # function to disconnect from the databse
    def disconnect(self):
        if self.conn:
            try:
                if self.conn.is_connected():
                    self.conn.commit()
                    self.conn.close()
                    print("Disconnected from the database.")
                else:
                    print("Connection is already closed.")
            except Exception as e:
                print(f"Error during disconnect: {e}") 
    
    # function to execute query        
    def execute_query(self, query, params):
        try:
            self.cursor.execute(query, params)
            print("Query executed: " + query)
            
            if query.startswith("SELECT"):
                return self.cursor.fetchall()
            
            self.conn.commit()
            return 
        
        except sql.Error as e:
            print(f"Error executing query: {e}")
            return None
        
    # function to fetch table
    def fetch_table(self, table):
        self.cursor = self.conn.cursor()
        query = "SELECT * FROM `" + table + "`" 
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
