class a:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    

    def show(self):
        return self.get_name(), self.__age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def change_age(self, age):
        if type(age) == str:            # here we are doing this nonsense bcoz we want avoid directly modifying the age
            age = int(age)
            self.__age = age
            print(f'Age Successsfully Changed To : {self.get_age()}')
        else:
            print('Not Allowed')


b = a('ashura', 55)

print(b.show())
# print(b.__name)
print(b._a__name)       # this is how you print private variables
# print(b.age)

b.area = 'Kanpur'       # this here created a new variable
print(b.area)

print(b.get_name())

print(b.get_age())

b.change_age(30)

b.change_age("30")


