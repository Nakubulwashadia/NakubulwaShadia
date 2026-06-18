#Mon 15-06-2026 
#MORNING SESSION
#DATA STRUCTURES
#SETS
#Usedto store a unique collection of data
#stores completely unquie data
#unordered collection
#support fast search

#example of a set
# cars = ('suzuki', 'honda', 'subaru')
# print(cars)
# print(type(cars))

#data uniqueness
# Name = {'shanita', 'Ketra', 'Sania', 10, 23, 34}
# print(Name)
# print(type(Name))

#data duplication
# letters = {"a", "b", "c", "c", "a", "a"}
# print (letters)
# print(type(letters))

#used of the add method
# letters.add("z")
# print(letters)

# Age = {20,30,24,'jackson'}
# students = {'jackie', 'jackson', 'brian', 'lola'}
# w=Age.union(students)
# print(w)
# print(type(w))

#intersection method
# i=Age.intersection(students)
# print(i)

#update method



#LISTS
#used to store ordered collection of items
#mutable i.e can be changes, added, updated
#store data of multiple data types

#creating a list
# a = [1,2,3,4,5,]
# print(a)
# print(type(a))

#example 2
#food=['posho','beans','cassava']
# print(food)
# print(type(food))

#Accessing an item in a list
# print(food[1])
# print(food[0])
# print(food[-3])

#use of a constructor to create a list
#Add item 
# food.append('rice')
# print(food)

#add item at a specific location
# food.insert(1,'kalo')
# print(food)

#updating elements into a list
# food[0] = 'matooke'
# print(food)

#removing an item
# food.remove('rice')
# print(food)

#popping an item
# popped_food = food.pop(1)
# print(food)
# print("popped_food:",popped_food)

#nested lists
# num = [[1,2,4,5],['a','b','c']]
# for row in num:
#     for item in row:
#         print(item, end=' ')
#         print(num)

#TUPLES
#immutable ordered collection of elements
#they are ordered, heterogenous

#create a tuple
# computers =('hph', 'mac', 'apple')
# print(computers)
# print(type(computers))

#demonstarte heterogenous
# names = ('kiran','rita',1,2,3)
# print(names)
# print(type(names))

#convert a list into a tuple

# list = [100,200,300,500]
# print(type(list))

# num = tuple(list)
# print(num)
# print(type(num))

# print(num[1])

#exercise
#how to delete a tuple
#how can a tuple be updated
#how to concatenate a tuple

#tuples are mutable
#change a tuple to a list first and then update, delete and later change to a tuple


#EVENING SESSION
#FUNCTIONS IN PYTHON
#parameters and arguments
#return statements
#scope of variables

#what is a function?
#is a reusable block of code that performs a specific task
#it allows us to organize code inot smaller manageable pieces and code reusability

#syntax of a function
# use def key word and function name eg def function-name(parameters):
#fuction body
#return type

#built-in fuctions
#print()
# len() returns length of an object
# type()
# range()

#example
# print('hello world!')
# len('hello')

#defining a function
#example 2:
# def greet():
#     print('welcome to python programming')

# greet()

#lab activity 2 mathematical function
#square of a number num=5

# def square_number():
#     num = 5
#     square = num * num
#     print(square)

# square_number()

#exercise 1: write a function that takes in input and calculate the area of a rectangle
# def rectangle_area(length,width):
#     length = float(input("Enter length: "))
#     width = float(input("enter width: "))                             #some error correct
#     area = length * width
#     print(area)

# rectangle_area(length, width)

#parameter and argument
# def greet user(name):
#     print(f'My name is ',{name})

# Arguments
# what are arguments?
# Arguments are actural values passed to a function
#e.g greet('Shadae Edits)

#A fuction with a single parameter
# def greet(name):      #(name) is a parameter
#     print(f'My name is', name)

# greet('Shadae Edits')    #(shadae edits) is an argument

#multiple parameters
# def add_numbers(a, b):
#     print(a + b)

# add_numbers(10, 2)


#exercise
# def display_info(name,age,course,student_number):
#     print('\nSTUDENT INFORMATION............')
#     print(f'name, age, course, student_number: ', name, age, course, student_number)
#     name = (input('Enter name: '))
#     age = int(input('Enter age: '))                                 #error
#     course(input('course: '))
#     student_number(input('student_number: '))
    

# display_info(name,age,course,student_number)

#positional arguments
# def display(name, age):
#     print(name)
#     print(age)

# display('Kana', 22)

#keyword argument
#arguments that can be specified using parameter name
# def display(name, age):
#     print(name)
#     print(age)

# display(name='Kana', age=22)


#default parameter
def display(name, age=24):
    print(name)
    print(age)

display('Kana')

#return statements
#sends a value back to the caller
# print()the value cannot be reused easily, return() code can be reused easily
def add(a,b):
    return a * b

result = add(5*10)
print(result)

#multiple return statement

#variable scope and the types
#global variable and local variable

#exe3 create a function that calculates the area of a circle
#exe4 write a program demonstrating the diff btn local n global variables
#Assignment


