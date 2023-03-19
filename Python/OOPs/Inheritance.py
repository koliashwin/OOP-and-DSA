# inheritance is a way to creating new calss for using details of an already existing class

class Humans:
    def eat(self):
        print("we can eat food")
    
    def sleep(self):
        print("we sleep to recover")

class kids(Humans):
    def play(self):
        print("we like to play")
    
class adults(Humans):
    def study(self):
        print("we need to study")

# create objects for kids class and adults class
kid1 = kids()
adult1 = adults()

# calling a function from inside the class
kid1.play()
adult1.study()

# calling the function form parent class
kid1.eat()
adult1.sleep()