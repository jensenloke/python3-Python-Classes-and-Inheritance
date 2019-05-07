##Qn1

class Bike:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.color = initX
        self.price = initY

testOne = Bike('blue',89.99)   
testTwo = Bike('purple',25.0)

##Qn2

class AppleBasket:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.apple_color = initX
        self.apple_quantity = initY
    
    def increase(self):
        return self.apple_quantity + 1
    
    def increase(self):
        self.apple_quantity = self.apple_quantity + 1
        
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)    

testOne = AppleBasket('red',4)
print(testOne)
testOne.increase()
print(testOne)

##Qn3

class BankAccount:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.name = initX
        self.amt = initY
    
    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name, self.amt) 

t1 = BankAccount("Bob",100)   
print(t1)

