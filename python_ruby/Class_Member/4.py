class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        result = self.v1+ self.v2
        Cal._history.append("add : %d+%d=%d" %(self.v1, self.v2, result))
        return result
    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" %(self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    @classmethod
    def history(cls):
        for item in Cal._history:

class Calmultiply(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("add : %d*%d=%d" %(self.v1, self.v2, result))
        return result
class CalDivide(Calmultiply):
    def devide(self):
        result = self.v1 / self.v2
        Cal._history.append("divide : %d/%d=%d" %(self.v1, self.v2, result))
        return result

c1 = Calmultiply(10,10)
print(c1.add())
print(c1.multiply())

c2 = CalDivide(20,10)
print(c2, c2.multiply())
print(c2, c2.divide())
Cal.history()
