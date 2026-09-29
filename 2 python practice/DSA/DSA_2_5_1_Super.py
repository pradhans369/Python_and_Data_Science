class User:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.__var = 5
        self.var2 = 22

    def login(self):
        print('Login')

    def register(self):
        print('Register')

    def get_var(self):
        return self.__var
    
    def show(self):
        print('Hii_parent')

class Student(User):
    def __init__(self, first_var, second_var, val):
        super().__init__(name=first_var, state=second_var)
        self.val = val
    # Here we had to use super to use the attribute of parent coz, if the child has any constuructor then the constructor of the parent class will not be called.

    # If the child class didnot had any constructor method, then the constructor of the parent would have been called

    def enroll(self):
        print('Enroll')
    
    def review(self):
        print('Review')
    
    def show(self):
        print('Hii_child')
    
    def parent_show(self):
        super().show()
    
    def check(self):
        print(self.var2)            # we can directly access the attribute of parent using "self.var"



# -------------------------------------------------------------------------------

# s1 = Student(12)
# print(s1.val)

s2 = Student('Jeet','Odisha',12)
print(s2.name)
print(s2.state)
print(s2.val)

s2.parent_show()
s2.register()

super(Student, s2).show()       # if there are two same methods in both parent and child class, then this is the way to directly call the method of the parent class

s2.check()