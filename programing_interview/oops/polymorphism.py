# What is Polymorphism? 

# Ans: Oject comes in different types of forms
# Button: round button, check button, square button, button with image. They do share a logic onClick()
# Accessing them using the same method called as polymorphism

# Method overriding

# Override means having two methods with same name doing differnet tasks
# It means that one of the method overrides the other
# If the is any method in the superclass and a method with the same name in a subclass, 
# then by executing the method, the method of the corresponding class will be executed

# Polymorphism is a fundamental concept in object-oriented programming (OOP) 
# that refers to the ability of different objects to respond to the same operation in 
# different ways. In simpler terms, polymorphism allows objects of different types to be 
# treated as objects of a common super type. This facilitates flexibility and integration
# in a codebase by enabling a single interface to be used for a general class of actions.


class Parent:
    name="scooter"

class Child(Parent):
    name="David"  #--> Overrided a variable
    pass

# Override a method

class Bank():
    def rateOfMethod(self):
        return 0

class ICICI(Bank):
    def rateOfMethod(self):
        return 10.5

obj=Child()
print (obj.name)

obj2 = ICICI()
print (obj2.rateOfMethod())

# Method Overloading (Compile-Time Polymorphism)
# Method overloading allows a class to have multiple methods with the same name
# but different parameters. However, Python does not support method overloading 
# in the traditional sense as seen in languages like Java or C++. 
# Instead, you can achieve similar behavior by using default arguments or variable-length arguments.
class Math:
    def add(self, a, b, c=0):
        return a + b + c

math = Math()
print(math.add(2, 3))    # Output: 5
print(math.add(2, 3, 4)) # Output: 9

# Method Overriding (Runtime Polymorphism)
# Method overriding occurs when a subclass provides a specific 
# implementation of a method that is already defined in its superclass. 
# The method in the subclass should have the same name, parameters, 
# and return type as the method in the superclass.

class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
# Output:
# Bark
# Meow
