def courses(*args):
  for subject in args:
    print(subject)
    
courses("big data","CCNA", "OOP2")
#keyword arguements
def courses(**kwargs):
  for key,value in kwargs.items():
    print("{}:{}".format(key, value))
#overriding arguements
def kenya(county = "mombasa"):
  print("i am from " + county)
kenya()
kenya("Nairobi")
kenya("kiambu")
kenya("kisumu")
#passing a list as an arguement
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple","banana", "cherry"]

my_function(fruits)
