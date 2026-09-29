# When we write x = 4/2, py automatically divides the numbers and assigns 2 to the x.
# Now we are going to create a datatype, that will store fraction x = 4/2 directly.
import math

class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ZeroDivisionError("DENOMINATOR CANNOT BE 0")
        self.num = n        # numerator
        self.den = d        # denominator

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        
        temp_fraction = "{}/{}".format(self.num, self.den)
        return temp_fraction

    
    def _to_fraction(self, val):
        if isinstance(val, int):
            return Fraction(val, 1)
        return val
    
    # --------------------------------------------------------------
    
    # fractional add
    def __add__(self, other):
        other = self._to_fraction(other)

        if isinstance(other, Fraction):     # this is to check for string inputs sent by user
            new_num = (self.num * other.den) + (other.num * self.den)
            new_den = (self.den * other.den)

            return Fraction(new_num, new_den)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    # --------------------------------------------------------------

    # fractional substraction
    def __sub__(self, other):
        other = self._to_fraction(other)

        if isinstance(other, Fraction):
            new_num = (self.num * other.den) - (other.num * self.den)
            new_den = (self.den * other.den)
            return Fraction(new_num, new_den)
        return NotImplemented
    
    def __rsub__(self, other):
        return self.__sub__(other)

    # --------------------------------------------------------------

    # fractional multiplication
    def __mul__(self, other):
        other = self._to_fraction(other)

        if isinstance(other, Fraction):
            new_num = (self.num * other.num)
            new_den = (self.den * other.den)
            return Fraction(new_num, new_den)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)

    # --------------------------------------------------------------

    def __truediv__(self, other):
        other = self._to_fraction(other)

        if isinstance(other, Fraction):
            new_num = self.num * other.den
            new_den = self.den * other.num
            return Fraction(new_num, new_den)
        return NotImplemented
    
    def __rtruediv__(self, other):
        other = self._to_fraction(other)        # For right-hand division (e.g. 3 / a), it is other / self
        return other.__truediv__(self)

    # --------------------------------------------------------------

    # simplifying a fraction
    def simplify(self):
        common = math.gcd(self.num, self.den)
        num = self.num // common
        den = self .den // common

        return Fraction(num, den)


# **************************************************************************************************
a = Fraction(4, 2)

print(type(a))
print(a)


b = Fraction(6, 8)

print(a.simplify())
print(a.num)
print(a.den)
print(a + 5)
print(4 + a)
print('SUBSTRACTION\n', a - 10)
print(b - a)
print('MULTIPLICATION\n', a * 33)
print(a * b)
print('DIVISION\n', a / 22)
print(b / a)

















