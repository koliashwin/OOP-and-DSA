# polymorphism (overloading, overriding)
# overloading : we use same function with different params in same class
# overriding : we can use same function with same parms in differnt class

class kids():
    def play(self):
        print("we play in sand")
    
    def study(self, sub1=None, sub2=None):
        if sub2 is None:
            if sub1 is None:
                print("we do fun")
            else:
                print("we study {}".format(sub1))
        else:
            print("we study {} and {}".format(sub1, sub2))
    
class adults():
    def study(self):
        print("we study books")
    
    def play(self):
        print("we play football")

# create objects for kids and adults
kid1 = kids()
adult1 = adults()

# overriding example call same function from both class
print("overriding :")
kid1.play()
adult1.play()

# overloading example call same function from same calss
# note : its little bit different in python
print("overloading :")
kid1.study("alphabets")
kid1.study()
kid1.study("numbers","poem")