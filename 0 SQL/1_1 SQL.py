import sys
from _0 import DBhelper

class Facebook:
    def __init__(self):
        # connect to the data base
        self.db = DBhelper()
        self.start()

    def start(self):
        """Main entry point to avoid recursion."""
        while True:
            user_input = input("""
                1. Enter 1 to register
                2. Enter 2 to login
                3. Anything else to leave
                            
    """)
            
            if user_input == "1":
                self.register()
            elif user_input == "2":
                self.login()
            else:
                print("Exiting...")
                sys.exit(0)

    def register(self):
        name = input('ENTER THE NAME : ')
        email = input('ENTER THE E-MAIL : ')
        password = input('ENTER THE PASSWORD : ')

        response = self.db.register(name, email, password)

        if response == 1:
            print("REGISTRATION SUCCESSFUL")
        else:
            print("REGISTRATION FAILED")

    def login(self):
        email = input("ENTER EMAIL : ")
        password = input("ENTER PASSWORD : ")
        data = self.db.search(email, password)
        
        if len(data) == 0:
            print("LOGIN FAILED: INCORRECT EMAIL OR PASSWORD")
        else:
            print("LOGIN SUCCESSFUL")
            print(f"Welcome {data[0][1]}!") # Assuming Name is the second column



if __name__ == "__main__":
    obj = Facebook()

