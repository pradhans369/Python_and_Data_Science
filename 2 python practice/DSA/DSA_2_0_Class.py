import sqlite3

class atm:
    # constructor : a special method that runs automatically, as soon as you make an object of the class
    def __init__(self):
        self.pin = int()
        self.balance = int()
        self.menu()
    # just like __init__ there are other "Dunder Methods" as well, that activates automatically as soon as the object is created

    # a Mehod is just a normal function which is mentioned inside a class and can only be called inside the object of the class
    # One method in class cant directly call another method in the same class, to do so you have to call the method using an object like "self." (self.methodName)
    
    def menu(self):
        user_input = int(input("""
HELLO ! HOW WOULD YOU LIKE TO PROCEED ?
    - ENTER 1 TO CREATE PIN \n
    - ENTER 2 TO DEPOSIT \n
    - ENTER 3 TO WITHDRAW \n
    - ENTER 4 TO CHECK BALANCE \n
    - ENTER ANY OTHER NUMBER TO EXIT ⚠️
        \n"""))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            print('WITHDRAW\n')
        elif user_input == 4:
            print('CHECK BALANCE\n')
        else:
            print('EXITED\n')


    # generating pin (must be int and four digit pin)
    def create_pin(self):
        temp = input("ENTER YOUR FOUR DIGIT PIN :\n")
        
        if len(temp) == 4 and temp.isdigit():
            self.pin = int(temp)
            print("\nPIN SUCCESSFULLY GENERATED\n")
            self.menu()
        else:
            print("\nINVALID PIN DIGITS ENTERED ⚠️, PLEASE TRY AGAIN.\n")
            self.create_pin()


    # generating deposit method
    def deposit(self):
            # 1. Ask for the PIN once at the very beginning
            temp_pin = input("ENTER YOUR PIN\n")
            
            if not (temp_pin.isdigit() and int(temp_pin) == self.pin):
                print(f"INCORRECT PIN ⚠️, TRY AGAIN.\n")
                self.deposit()
                return 

            # 2. If the PIN is correct, enter a loop for transactions
            while True:
                amount = input("ENTER AMOUNT\n")

                if amount.isdigit() and int(amount) > 0:
                    pre_balance = self.balance
                    self.balance = self.balance + int(amount)
                    print(f"\nSUCCESSFULLY DEPOSITED\nBALANCE BEFORE : {pre_balance}\nBALANCE NOW : {self.balance}\n")
                    
                    choice = input("TO ADD MORE MONEY ENTER 'Y', \nTO EXIT ENTER 'N': \n\n").upper()
                    
                    if choice == 'Y':
                        print("\n--- Preparing Next Deposit ---")
                        continue        # if the user wants to add more money, the loop will run again
                    else:
                        print("RETURNING TO MAIN MENU...\n")
                        self.menu()
                        break 
                        
                else:
                    print(f"\nINVALID AMOUNT ENTERED ⚠️")







# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------


a = atm()





