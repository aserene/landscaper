print("hello world")
# This is a comment


##################
### Variables ###
##################

## Variables that never change should be written in all uppercase
THIS_CONSTANT = 5

## All other variables will use snake case
this_variable = "uses all lowercase and is separated with underscores"

print(THIS_CONSTANT)
print(this_variable)

# How to take in User input
user_input = input("Who are you?")
print(user_input)

# syntax for using interpolation: put 'f' before quotation marks
print(f"Hey there {user_input}")

# how to write conditionals
num = 2 
if (num < 2):
    print("num is less than 2")
elif (num > 2):
    print("num is greater than 2")
else:
    print("num is 2")

# how to write loops
counter = 0
while(counter <10):
    print(counter)
    if (counter % 2 == 0):
        print("its even")
    elif (counter % 2 == 1 and counter % 3 == 0):
        print("meow")
    else: 
        print("nothing")
    counter += 1
