# Abstract class

# Abstract classes are classed that contain one or more abtract methods. 
# An abstract method is a method that is declared, but contains no implementation. 
# Abstract classes cannot not be instantiated, and require subclasses to provide implementation for the abstract methods
# Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class. 

from abc import ABC

class FoodChain(ABC):
    @classmethod
    def food(self):
        pass

    @classmethod
    def eat(self):
        pass
    @classmethod
    def poop(self):
        pass

# Parent class
class Meal(FoodChain):
    def food(self):
        print ("Food is Non-Veg")
    def poop(self):
        print("Tiger popped")

#Sub class
class Tiger(Meal):
    def eat(self):
        print("Tiger Eat Non-Veg")



t=Tiger()
t.food()
t.eat()
t.poop()