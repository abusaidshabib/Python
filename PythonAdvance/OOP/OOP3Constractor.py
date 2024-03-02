#Constructor with parameter
# without params
class Mobile:
    def __init__(self):
        self.model = "Redmi 7s"

    def show_model(self):
        print("Model:", self.model)

redmi = Mobile()
redmi.show_model()


# with params
class Mobile:
    def __init__(self, model, version=80):
        self.model = model #instance Variable = Instance variables are the variables whose separate copy is created in every object. Instance variable are defined and initialized using a constructor with self parameter.
        self.version = version

    def show_model(self, price):
        price = price
        print("Model:", self.model, "and Price: ", price)
        print('Version: ', self.version)

redmi = Mobile('Redmi 7s', 50)
redmi.show_model(1000)
print()
realme = Mobile('Realme X')
# change instance variable
realme.model = 'Samsung X'
realme.show_model(2000)


