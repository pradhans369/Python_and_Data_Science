class customer:
    __id = 1          # This is a static variable

    def __init__(self, name):
        self.name = name
        self.__id = customer.__id           # accessing static variable
        customer.__id += 1                # will set different customer id for different customers


    @staticmethod
    def get_id():
        return customer.__id        # you dont need an obj to call the static variable (no need for self.customer.__id)




# ----------------------------------------------------

cust = customer('jeet')

print(cust.name)



def greet(obj):
    print(f"Hello {obj.name}")

greet(cust)

print(cust.get_id())


cust2 = customer('Ashura')
print(cust2.name, cust2.get_id())

cust3 = customer('Rocky')
print(cust3.name, cust3.get_id())

print(customer.get_id())
print(customer.get_id())


