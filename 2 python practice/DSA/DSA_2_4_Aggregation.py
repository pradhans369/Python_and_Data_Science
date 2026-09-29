# Learning Aggregation : Aggregation is a design relationship where one class contains or refers to another class, representing a "Has-A" relationship

class Customer:
    def __init__(self, name, gender, add):
        self.name = name
        self.gender = gender
        self.address = add
    
    # changing the details
    def change(self, city, pincode, state, name=None, gender=None):     # if no name is assigned self.name will be assigned
        if name is not None:
            self.name = name
        if gender is not None:
            self.gender = gender

        # changind the address by calling the "change_address" method in Address class
        self.address.change_address(city, pincode, state)

    def show(self):
        print(self.name, self.gender, self.address.city, self.address.pincode, self.address.state)

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

# ------------------------------------------------------------------------

add1 = Address('Bhubaneswar', '147852', 'Odisha')

c1 = Customer('Jeet', 'Male', add1)

print(c1.address)               # will only print the address in the memory coz, it only holds the address of another obj from 'Address' class
print(c1.address.city)
print(c1.address.pincode)
print(c1.address.state)

c1.change('Sambalpur', '546565', 'Odisha', 'Ashura')

c1.show()




 




