# syntax for declaring variable
# var_name = value
myVar = "im here"
print("initial value:",myVar)

# you can also overwrite the data into myVar with following syntax
myVar = 568749
print("new value:", myVar)

# variables are case sensitive and you can assign multiple values to multiple variables
# below i've use the same word with different combination of capital and small letters and assigned the value in same line
myAge, myage, MyAge = 18, "twenty four", 36.7
print(myAge, myage, MyAge)

# correct way of naming variables
'''
myvar = "some value"
Myvar = "some value"
_myvar = "some value"
my_var = "some value"
myvar01 = "some value"
my_01_var = "some value"
'''

# invalid ways of naming variables
'''
01myvar = "some value"
my-var = "some value"
my var = "some value"
'''