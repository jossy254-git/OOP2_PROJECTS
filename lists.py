#list() constructor
fruits = list(("orange", "mango", "banana", "orange"))
print(fruits)

#lists data types
list1 = ["string"]
list2 = [1, 2]
list3 = [True, False,]
list = ["apple", 1, True]

#list inside a list
list1 = [1,2,3,4, ["apple", "orange"],[True, False]]
print(list1)

#geting items
print(list1[1])
print(list1[:])
print(list1[0:-1])

#check if item exists
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
  print("yes, 'apple' is in the fruits ")
