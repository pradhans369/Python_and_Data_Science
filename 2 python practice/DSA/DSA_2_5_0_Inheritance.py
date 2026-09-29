# Inheritance
# as child class, you can access the methods and attributes (only public attributes not private, can be possible only via a getter method) of parent class, but not vice-versa


class User:
    def __init__(self, name):
        self.name = name
        self.__var = 5

    def login(self):
        print('Login')

    def register(self):
        print('Register')

    def get_var(self):
        return self.__var
    
    def show(self):
        print('Hii_parent')

class Student(User):        # inheriting parent (can inherit multiple classes -- [Student(Parent_1, Parent_2)])
    def enroll(self):
        print('Enroll')
    
    def review(self):
        print('Review')
    
    def show(self):
        print('Hii_child')

# ----------------------------------------------------------------------------------


s1 = Student('Ashura')      # Since the Student class does not define its own __init__ method, it automatically inherits the constructor of its parent class User. 

# Hence we must have to define the name as it have inherited the constructor of the parent class

s1.login()      # accessing parent class methods
s1.register()

print(s1.get_var())
print(s1._User__var)


s1.show()               # if there are two common methods in parent and child, by calling the show method it will first search for show method in child class (if called via child obj), and will execute it. It show were not present in child class, then it would have search for show method in parent class and would have executed that


s2 = Student('Jeet')
print(s1.name)





