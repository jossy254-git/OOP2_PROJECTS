#change list items
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits[1] = "blackcurrent" # change the second item
print (fruits)

fruits[1:3] = ["watermelon"]

# add list items
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits.append('orange')
print(fruits)

#loop through a list
#print all items in the list, one by one 
fruits = ['apples', 'banana', 'cherry']
for x in fruits:
  print(x)
  
# use the range () and len() function to create a suitable iterable
for i in range (len(fruits)):
  print(fruits[i])
