# function syntax: def name_of_function
def add_nums(x,y):
    return x + y
print(add_nums(5,7))
# sub_nums that takes two arguments and returns their difference
def sub_nums(a, b):
    return a - b
print(sub_nums(10, 2))
# say_hello that takes a name as an arguments and says hello to that name
def say_hello(name):
    return f"Hello {name}"
print(say_hello("athena"))
# sayhelloadv that takes a dictionary with a name and age property and prints "hello {name}, how does it feel to be {age} years old"
def sayHello(name, age):
    return f"Hello {name}, how does it feel to be {age} years old?"
print(sayHello(name="Athena", age = 25))
def say_hello_adv(dict):
    print(f"hello {dict['name']}, how does it feel to be {dict['age']} years old?")
say_hello_adv({"name": "Athena", "age": 25})
#loop that takes an array as an argument, it loops over the array and prints each item individually
list = [1,2,3]
def loop(array):
    for item in array:
        print(item)
print(loop(list))
loop([1,3,5,7])



## Lamda (Arrow Function)
#def iNeedACallback(cb):
    #cb(5)
    
#iNeedACallback(lambda x:print(x))