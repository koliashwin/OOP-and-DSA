# Encapsulation reffers to bundling of attributes and methods inside a single class.

class Computer:
    def __init__(self):
        self.__maxprice = 1000
    
    def sell(self):
        print("selling price is {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice=price

# create object n call a function
c = Computer()
print("initial price")
c.sell()

# change the price and call a fuction
c.setMaxPrice(2500)
print("updated price")
c.sell()