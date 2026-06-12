#12 - 06- 2026

#BOOLEAN (AND & OR OPERATOR)
#a=1
#b=2
#c=4
#if a > b and  b < c:
#    print(True)
#else:
#    print(False)

#if a and  b or c:
#    print("At least one number has a boolean value as True")


#EQUIVALENT AND NOT EQUIVALENT OPERATOR
#a=0
#b=1
#if(a==0):
#    print(True)
#else:
#    print(False)

#if (a == b):
#    print (True)
#else:
#    print(False)

#if (a != b):
#    print (True)
#else:
#    print(False)


# IS OPERATOR AND IS NOT
#x=10
#y=1

#if x is not y:     #u can put there is
#    print(True)
#else:
#    print(False)


#PYTHON KEYWORDS
# YOU CAN GET THE LIST OF AVAILABLE KEYWORDS BY USING help()


# Data types eg numeric (floats, complex, int), boolean, dictionaries, set, sequence type
#Dictionary
#these store information in keyvalue pairs
#properties - 
#1 they are immutable and mutable

#data = {
#    "x" : 1,
#    "y" : 30   #NOT A DICTIONARY

#}
#print(data)

#using dict function
# b = dict(name = "Sam", age = 17)
# print(b)

#Accessing the Dictionary item
#print(b["name"])

#Using get method
#print(b.get("age"))

#Adding and Updating dictionary item
#Removing dictionary items
#del b["name"]
#print(b)

#Using pop() method
# num = b.pop("age")
# print(num)

# Nesting: Having a dictionary within another dictionary.
# Iterating through a dictionary

# Students = {
#     "student1": {
#         "name": "Shadia",
#         "age": 23,
#         "city": "Kampala"
#     },
#     "student2": {
#         "name": "Rinah",
#         "age": 21,
#         "city": "Kampala"
#     }
# }

# print(Students)



#EVENING SESSION
#LOOPS IN PYTHON
#why use loops?
#1. To repeat a block of code multiple times.

#Example 1
#without loops
# print ("Day 1:python")
# print ("Day 2:python")
# print ("Day 3:python")
# print ("Day 4:python")

#with loops
# fruits = ["mangoes", "oranges", "bananas", "grapes"]
# for fruit in fruits:
#     print(f"I like {fruit}")

#exercise 1
#for i in range(1, 11):
#      print(f"num{i}")
#      print

#exercise 2
books = ["The Alchemist", "The Power of Now", "The Monk Who Sold His Ferrari", "The 5 Love Languages"]
for book in books:
    print(f"I like {book}")