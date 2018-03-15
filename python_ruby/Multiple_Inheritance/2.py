class Calmultiply():
    def multiply(self):
        return self.v1*self.v2
class CalDivide():
    def devide(self):
        return self.v1/self.v2

class Cal(Calmultiply, CalDivide):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1 + self.v2
    def subtract(self):
        return self.v1 - self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

c=Cal(100,10)
print(c.multiply)
