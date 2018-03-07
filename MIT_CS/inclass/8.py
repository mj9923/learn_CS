class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

c = Coordinate(3, 4)
zero = Coordinate(0,0)
print(c.distance(zero))
print(Coordinate)
print(type(Coordinate))
print(c)
print(isinstance(c,Coordinate))

class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)

    def __float__(self):
        return self.num/self.denom

    def inverse(self):
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c=a+b
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse( )))
