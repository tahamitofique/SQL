import mysql.connector
import sys


class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occured. Could not connect to database")
            sys.exit(0)
        else:
            print("Connected to Database")

    def login_menu(self):
        pass

    def register(self, name, email, password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`ID`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')""".format(name, email, password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self, email,password):
        self.mycursor.execute("""
        SELECT * from users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))

        data = self.mycursor.fetchall()

        #print(data)
        return data
