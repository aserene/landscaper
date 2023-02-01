## equivalent of a javascript array is a list
my_list = [1,2,3]
print(my_list)
print(my_list[1])

# equivalent of javascript object is called a dictionary
my_dictionary = {"cheese": "gouda", "bread": "rye"}
print(my_dictionary)
print(my_dictionary["cheese"])

# How to find the length of a list
list = [1,2,3,4,5,6,7,8,9,10]
print("Lenth:", len(list))
# how to loop thru a list
for num in list:
    print(num)
# how to add/remove from a list
list.append(11)
print(list)
list.insert(0, 0)
print(list)
list.remove(7)
print(list)