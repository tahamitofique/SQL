import sys
from dbhelper import DBhelper


class Flipkart:
    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to Register
        2. Enter 2 to login
        3. Anything else to leave
        """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input("Enter the Name:")
        email = input("Enter the Email:")
        password = input("Enter the Password:")

        response = self.db.register(name, email, password)

        if response:
            print("Registration Successful")
        else:
            print("Registration Failed")

        self.menu()

    def login(self):
        email = input("Enter Email:")
        password = input("Enter Password:")
        data = self.db.search(email, password)
        #print(len(data))

        if len(data) == 0:
            print("Incorrect Email/Password")
            self.login()
        else:
            print("Hello", data[0][1])


obj = Flipkart()
