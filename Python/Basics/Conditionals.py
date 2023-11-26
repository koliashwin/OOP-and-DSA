# there are mainly 3 types of conditional statements namely If...Else statements, Loops and Switch Case statment


# --------------------------------------IF Else Statements-----------------------------------------

# If...else statement is mainly used to redirect the flow as per logical conditions
'''
following are the mostly used logical conditions in If...Else statements:
    
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    greater than: a > b
    Greater than or equal to: a >= b
'''



myAge = 24      # test variable
myCast = "open"
myGender = "male"

# to check single condition use "If Statment"
print("----------If Statement-----------")
if myAge > 18:
    print("I'm eligible to vote")



# to check multiple conditions and choose 1 option use "If Else statment", 
# you can use "elif" just like "if statement" to check multiple conditions
print("---------If Else statement---------")
if myAge < 18:
    print("im young")
elif myAge >= 18 and myAge < 50:        # you can use key words like 'and','or' to validate different set of conditions as per your requirment
    print('im adult')
else:
    print("im old")



# to check multiple conditions use multiple "if Statements"
# here all conditions are independent of each other
print("----------Multiple if statements----------")
if myAge > 18:
    print("I'm adult now")
if myGender == "male":
    print("I'm a man")
if myCast == "open":
    print("I belong to open category")



# to check conditons inside a condition use "Nested if statment"
# here the 2nd condition is dependent on 1st condition
print("----------Nested if statement----------")
if myAge > 18:
    print("you are eligible for this entrence test")
    if myCast == "open":        # this print statement will only execute if both above and this conditions are true
        print("and you need to pay Rs.1000/- and you need to score 40% more marks than others to secure a seat.")



# short hand "If...Else"
print("----------ShortHand if statement----------")
# [result when condition is true] if (condition) else [result when condition is false]
print("I can create memes") if myAge > 18 else print("I can only watch memes")

# -------------------------------------------------------------------------------


# -------------------------------------------Loops------------------------------------
# loops are used to iterate over a perticular range as per specific conditions
# python has 2 types of loops namely "for loops" and "while loops"

# using while loop we can execute the set of statements as long as the condition is true

numbers = [1,5,8,6,3,7,9,0]         # defined random array; will use this for all examples in while loop

print("\n------------------------simple While loop------------------------\n")
i = 0                               # defined starting index of loop (kind of an index pointer)
while numbers[i] != 7:              # condition (check if value at 'i'th index != 7 )
    print(numbers[i])               # print all values up until 7             
    i += 1                          # increment in index pointer



print("\n------------------------break statement in while----------------------\n")
i = 0                               
while numbers[i] != 7:              # condition (check if value at 'i'th index != 7 )
    print(numbers[i])               # print all values up until 7
    if numbers[i] == 6:
        print("used break")         # noticed loop stoped in the middle its because of break
        break                       # can use the break statement to break out of loop
    i += 1                          # increment in index pointer



print("\n------------------------continue statement in while--------------------\n")
i=0
while numbers[i] != 7:              # condition (check if value at 'i'th index != 7 )
    if i == 2:
        print("used continue in place of 8")         # noticed loop skipped the iteration; its because of continue
        i += 1
        continue                    # you can use the continue statement to skip iteration
    print(numbers[i])               # print all values up until 7
    i += 1                          # increment in index pointer

# -----------------------------------For Loop----------------------------------------

# "for loop" is used to iterat over a perticular string or a sequence (i.e. either list, tuple, set or dictionary)
# with "for loop" we can execute a set of statements, once for every item in a sequence

# Note: a sequence = any one of [list, set, dict, tuple]

# following are the variables, will use in examples for 'For loop'
myString = "someString"
myArray = ['red', 'blue', 'green', 'orange']

print("\n------------------------for loop without range()------------------------\n")

print("iteration over list :", end=" ")
for i in myArray:                   # when we don't provide the range; it will stores an item(in case of sequence)
    print(i, end=", ")              # print the result and end with comma and space


print("\niteration over String :", end=" ")
for i in myString:                  # when we don't provide the range; it will stores a letter(in case of string)
    print(i, end=", ")

# we can use break and continue keywords in "for loop" as well; functionality is same as it was in while loop


print("\n------------------------for loop with range()------------------------\n")
# range(lower_bound, upper_bound, step):- range() function can have from 1 to upto 3 values
#       lower_bound is inclusive i.e. program will consider minimum index = lower_bound
#       upper_bound is exclusive i.e. program will consider maximum index = upper_bound - 1
#       step is the increment in index pointer by default its 1

# if we provide only 1 value in range function it'll be considered as upper_bound. in this case lower_bound = 0 bydefault; i.e. range(0, your_value, 1)
# if we provide only 2 values in range function; 1st value = lower_bound, and 2nd value = upper_bound. in this case step = 1 bydefault; i.e range(value1, value2, 1)
# or you can provide all 3 values as per your requirments


print("range function with 1 param : ", end="")
for i in range(10):             # as we can see here; range(10) will iterate from 0 to 9 both inclusive
    print(i, end=" ")


print("\nrange function with 2 param : ", end="")
for i in range(5,10):             # as we can see here; range(5, 10) will iterate from 5 to 9 both inclusive
    print(i, end=" ")

print("\nrange function with 3 param : ", end="")
for i in range(0, 10, 2):             # as we can see here; range(0,10,2) will iterate over ever 2nd integer form 0 to 9 inclusive
    print(i, end=" ")
# -------------------------------------------------------------------------------


# switch case Statement
'''
python < 3.10 doesn't have a switch statement 
switch statement is similar to "If Elif Else statments"

syntax:

switch(argument){
    case 0:
        return "something, you can even write some conditon in place of 0";
    case 1:
        return "somethins for case 1"
    default:
        return "this will get executed it none of the conditions are true"
}
'''
