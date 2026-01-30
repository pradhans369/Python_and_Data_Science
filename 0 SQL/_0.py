import mysql.connector      # This is a standard driver (library) used to connect a Python application to a MySQL database. It allows the Python code to send SQL commands to the database server.
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='0_new_database')      # establishes the actual connection to your database server.

            self.mycursor = self.conn.cursor()
        except:
            print('ERROR : NOT CONNECTED TO THE DATABASE')
            # remember it will throw error when you give wrong intput and also when the server is down
            sys.exit(0)
            # 0 -- is the exit code for database error 
        else:
            print('\nSUCCESSFULLY CONNECTED TO THE DATABASE') 
        
    
    def register(self, name, email, password):
        # here you have to write SQL query
        try:
            # this is a way to register a new person into the database
            # Using parameterized queries to prevent SQL injection
            query = "INSERT INTO `users` (`User ID`, `Name`, `E-Mail`, `Password`) VALUES (NULL, %s, %s, %s)"
            self.mycursor.execute(query, (name, email, password))
            self.conn.commit()
        except Exception as e:
            print(f"Error during registration: {e}")
            return -1
            # -1 means there is an error
        else:
            return 1
            # 1 means everything has been done successfully
    
    def search(self, email, password):
        self.mycursor.execute("""
                              SELECT * FROM users WHERE E-Mail like '{}' AND Password LIKE '{}' """.format(email, password))
    
        data = self.mycursor.fetchall()
        print(data)