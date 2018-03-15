class C1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("C1 m")

class C2(object):
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")

class C3(C1, C2):
    pass

c=C3()
c.c1_m()
c.c2_m()
c.m()
