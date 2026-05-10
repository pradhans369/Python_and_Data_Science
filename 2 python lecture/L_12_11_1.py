"""
The '@property' decorator in Python is used to turn a method into a read-only attribute (variable).

    - Instead of calling a method with (), you can access it like an attribute.
    - It allows you to define computed attributes that look like normal variables but are calculated dynamically whenever accessed.
    - It is part of Python's encapsulation mechanism, letting you hide implementation details while providing a clean interface.

    
    USE CASE
    Dynamic Calculations
        - When an attribute depends on other attributes and should always stay updated.
        - Example: A circle's area and circumference depend on its radius. Instead of storing fixed values, use @property to calculate them whenever needed.

    Encapsulation and Validation
        - You may want to restrict direct access to attributes but still provide a way to get or set them in a controlled manner.
        - Example: Prevent negative values for salary or age.

    Cleaner API / Interface
        - With @property, users of your class don't need to know it's a method — they access it like an attribute, which makes your class easier to use.


"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)


# -----------------------
# Using the Rectangle class
# -----------------------

r1 = Rectangle(10, 5)
print("Length:", r1.length)
print("Width:", r1.width)
print("Area:", r1.area)             # ✅ property, no parentheses
print("Perimeter:", r1.perimeter)

print("-------------------------------------------------")

# Change dimensions
r1.length = 12
r1.width = 8
print("Updated Length:", r1.length)
print("Updated Width:", r1.width)
print("Updated Area:", r1.area)     # ✅ auto-updates
print("Updated Perimeter:", r1.perimeter)





















