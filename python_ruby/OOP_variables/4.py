class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
    def getValue(self):
        return self.value
    def setValue(self, v):
        self.value = v

c1 = C(10)

c1.show()
