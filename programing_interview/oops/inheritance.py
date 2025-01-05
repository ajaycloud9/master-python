#Inheritance
#Parent Class | Base Class | Super Class
#Sub Class | Derived Class 

#Example - Single Inheritance

class A:
    x,y = 100,20
    def m1(self):
        print ("This is a m1 method in class A")
        print (self.x + self.y)

class B(A):
    a,b=20,20
    def m2(self):
        print("This is a m2 method from class B")
        print(self.a + self.b)

aobj = A()
aobj.m1()

bobj = B()
bobj.m2()
bobj.m1()

#Example - Multiple Level Inheritance

class C(B):
    i,j=1,2
    def m3(self):
        print("This is a m3 method from class C")
        print(self.i + self.j)

cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()

# Example - Heirarchical Level Inheritance
# Note: X is the parent for both Y an Z class
# However, Y and Z can't access each other method
# And Attributes.
class X:
    x,y = 10,20
    def mx(self):
        print ("This is a mx method in class X")
        print (self.x + self.y)

class Y(X):
    a,b=20,20
    def m2(self):
        print("This is a m2 method from class Y")
        print(self.a + self.b)

class Z(X):
    i,j=1,2
    def m3(self):
        print("This is a m3 method from class Z")
        print(self.i + self.j)

xobj = X()
xobj.mx()

yobj = Y()
yobj.m2()
yobj.mx()

zobj = Z()
zobj.mx()
zobj.m3()

class MultiInheritance(A,X):
    aa,bb=11,22
    def m4(self):
        print("This is a m4 method from class MultiInheritance")
        print(self.aa + self.bb)

mi=MultiInheritance()
mi.m4()
mi.m1()
mi.mx()