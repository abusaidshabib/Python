# If we write in the both classes, parent class and child class then the parent class constructor is not available to the child class.
"""
In this cas only child class constructor is accessible which means child class constructor is replacing parent class constructor. Constructor overriding is used when programmer want to modify the existing behavior of a constructor
"""

class Father:
    def __init__(self):
        self.money = 2000
        print("Father Class Constructor")
    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init_(self):
        self.money = 5000
        self.car = 'BMW'

    def disp(self):
        self.money = 5000
        print("Son Class Constructor", self.money)

s = Son()
s.disp()