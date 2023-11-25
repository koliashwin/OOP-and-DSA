
# ---------------Numeric Datatypes----------------
print("---------Numerics----------")
# int: contains integer or a whole number, positive or negative, without decimals
# float: contains decimal numbers, positive or negative
# complex: contains complex numbers with real and imaginary parts (imaginary part written with "j")

x = 785     # int
y = 2.83    # float
z = 7 + 2j  # complex

# we can also convert these numbers from one data type to another. this process called the type casting
"Note: you cannot convert complex number to another numeric type"
print("integer x :", x)                 # initial int
print("decimal x :", float(x))          # to float
print("complex x :", complex(x))        # to complex
print("string  x :", str(x))            # to string
print("boolean x :", bool(x))           # to boolean
# --------------------------------------------------

# ---------------String Datatype----------------
print("---------String-----------")

# python strings are surrounded by either single or double quotes

myString = "Hey There"
print("myStirng : ",myString)

# you can access perticular letter in string useing associated index
print("first letter in 'myString':", myString[0])

multiline_String = '''This is multiline Stirng
you can use it to store text in specific format
for eg. poems of paragraphs.'''
print(multiline_String)
# --------------------------------------------------

# ---------------Boolean Datatype----------------
print("---------Boolean-----------")
# Booleans represent one of the two values: True or False. this highly used in conditional statements.

myAge = 23
if(myAge > 18):         # if condition is satifies then boolean value is true
    print("I can vote")
else:
    print("I'm not eligible")

# almost all the values are evaluated to be "True" if it has some sort of content
print("boolean value of 'sdec':", bool("sdec"))
print("boolean value of '574':", bool(574))
print("boolean value of '['red','blue','green']':", bool(['red','blue','green']))

# some "false" boolean value examples
print("boolean value of 'False'(keyword):", bool(False))
print("boolean value of 'None'(keyword):", bool(None))
print("boolean value of 0:", bool(0))
print("boolean value of ''(empty string):", bool(""))
print("boolean value of '()'(empty paranthesis):", bool(()))
# --------------------------------------------------

# ---------------List Datatype----------------
print("---------Lists-----------")

# Lists are used to store multiple items into single variable. Lists are mutable in python means we can modify list data once its created.
# we can declare a list as follows in python

# Note: list are not same as array. the key difference is List can store items of multiple datatypes while arrays can only store items form single datatype.
myList = ['red', 'blue', 'green', 125, False, 2-5j]
print("myList : ",myList)
# --------------------------------------------------

# ---------------Tuple Datatype----------------
print("---------Tuples-----------")

# A Tuple is a collection which is ordered and unchangable and also allows dublicatevalues. they are written in roun brackets.
myTuple = ('red', 'yellow', 'orange')
print(myTuple)

# to cerate tuple with single element you need to add comma after first item
single_ele_tuple = ("item1",)
print(single_ele_tuple, type(single_ele_tuple))
# --------------------------------------------------

# ---------------set Datatype----------------
print("---------Sets-----------")

# Set items are unordered, unchangeable, and do not allow duplicate values. still you can remove add new items to set
mySet = {'red','blue','black', 1, 5, True, False, True, 0, 5, 'red'} 
print(mySet)    # notice here 1 is remain and True was removed its becaue they both has same boolean values, same can be said for 0 and false. also the order was suffeled.
# --------------------------------------------------

# ---------------Dictionarie Datatype----------------
print("---------Dictionaries-----------")
# dictionaries used to store data into key: value pairs.
# A dictionary is a collection which is orderd, changeable and doesn't allow duplicates.
myDict = {
    "name" : "john Doe",
    "company": "xyz.inc",
    "Joining_year": 2025,
    "name": "Reika"
}
print(myDict)   # notice 'name: Reika' in output it happened because dictionary doesn't allow duplicates and simply overwrites the vale with newer data