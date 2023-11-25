# lets do famous "hello world" 
# syntax to print a string
print("hello world!")

# indentations are important in python
# following code will be executed properly
if 3 < 5:
    print("Three is less than 5")

# below code will thorw an error due to indentations
# you can remove the qoutes form below example and try it
"""
if 3 < 5:
print("three is less than five") 
"""

# note: 
# you can use any number of spaces after a colon(:) 
# but you need to user same number of spaces throughout 
# the block

# correct eg:
if 1<2 :
 print("something here")
 print("second statement")
if 2>1 :
        print("again something here")
        print("again second statement")

# wrong eg:

"""
if 1<2 :    # eg 1
 print("something here")
    print("second statement")

if 2>1 :    # eg 2
    print("again something here")
 print("again second statement")
 """