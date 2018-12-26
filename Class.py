class Point():
    ## Constructor
    def __init__(self, x, y):
        ## Attributes
        self.x = x
        self.y = y

    ## Define the METHODS of class Point
    def __str__(self):
        """Defines print(self)"""
        return "Point: <{}, {}>".format(self.x, self.y)

    def __repr__(self):
        """Defines the console output"""
        return "The Point is at location: <{}, {}>".format(self.x, self.y)

    def __add__(self, other):
        """Defines + """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Defines - """
        return Point(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """Defines negation (e.g. -Point)"""
        return Point(-self.x,-self.y)

    # equality operators:
    
    def __eq__(self, other) -> bool:
        """Defines == """
        return (self.x ** 2 + self.y ** 2) == (other.x ** 2 + other.y ** 2)

    def __ne__(self, other) -> bool:
        """Defines != """
        return (self.x ** 2 + self.y ** 2) != (other.x ** 2 + other.y ** 2)

    def __gt__(self, other) -> bool:
        """Defines > """
        return not (self <= other)

    def __lt__(self, other) -> bool:
        """Defines < """
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)

    def __le__(self, other) -> bool:
        """Defines <= """
        return self < other or self == other

    def __ge__(self, other) -> bool:
        """Defines >= """
        return not (self < other)
    
if __name__ == "__main__":

    # Defining and Instantiating my Object Point
    p = Point(1, 2) # Created object p of type Point
    q = Point(2, 0) # Created a second object p of type Point
    ## Both objects have different attributes/properties

    ## Testing my methods
    result_add = p+q
    print("The result of p+q is: ", result_add)
    result_sub = p-q
    print("The result of p-q is: ", result_sub)
    result_neg_p = -p
    print("The result of -p is: ", result_neg_p)

    print(p > q)
    print(p >= q)
    print(p < q)
    print(p <= q)

    print(p == q)
    print(p != q)

import math

class Rational():
    def __init__(self, numer: int, denom: int):
        gcd = math.gcd(numer, denom)
        self.numer = numer // gcd
        self.denom = denom // gcd
    
    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __neg__(self):
        return Rational(-self.numer, self.denom)
    
    def __invert__(self):
        return Rational(self.denom, self.numer)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom )

    def __truediv__(self, other):
        return self * ~other

    def __sub__(self, other):
        return self + -other

#equality operators:
# __lt__ , __gt__ , __le__ , __ge__ , __eq__ , __ne__

if __name__ == "__main__":
    p = Rational(2, 4)
    q = Rational(1, 7)
    print(p + q)
    print(p - q)  
    print(p * q)
    print(p / q)