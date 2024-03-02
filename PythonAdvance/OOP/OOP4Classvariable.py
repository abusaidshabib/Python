# Accessing class/static variable
"""
To access class variable, we need class methods with class as first parameter then we can access class variable using class variable_name
structure:

class Mobile:
    value1 = 'ClassVariable;
    fp = 'Yes' #class variable
    def ___init___(self):
        self.model = 'RealMe X'
    
    def show_model(self):
        print(self.model)
    
    #class method
    @classmethod
    def is_fp(cls):
        cls.fp

    realme = Mobile()
    # access class variable using Classname.variable_name
"""

class Mobile:
    fp = 'Yes' #class variable
    def ___init___(self):
        self.model = 'RealMe X'
    
    def show_model(self):
        print(self.model)
    
    #class method
    @classmethod
    def is_fp(cls):
        cls.fp

realme = Mobile()
realme.is_fp()