#22nd-06-2026
#MORNING SESSION
#OOP
#CLASSES
#The __init__() method function that is part of a class
#defining a class: class keyword Class name
# an object is a specific instance of a class. it can have its own methods, parameters, data. 
#multiple objects can be using same class.
# class Dog:
#create an object from class
#  name = 'kitty'
#  name1 = 'Rodger'
# dog1 =Dog()

# print(dog1.name)
# print(dog1.name1)

#Example 2
# class Student:
#     name = 'Shadia'
#     Nationality = 'Kenyan'

#how to apply the __init__()
#self refers to the current object and stores the current object's data
    # def __init__(self,age,religion):
    #     self.age=age
    #     self.religion=religion

#create an object
# student1 = Student(21,'Born again')

# print(student1.religion)
# print(student1.age)

#exercise
class Book:

#class variables
    title = 'Bible'
    Author = 'Multiple'
    num_book = 0

    def __init__(self,volume,price):

#instance variables
        self.volume=volume
        self.price=price
        Book.num_book += 1

book1 = Book(2,240000)
book2 = Book(3,300000)

print('Book title: ',Book.title)  #class variables are accessed through the class name
print('Book Author: ',Book.Author)
print('Book volume: ',book1.volume)  #instance variables are accessed through the instance name
print('Book price: ',book1.price)
print('Total books: ',Book.num_book)

# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type                              #not completed
    
#     def describe_restaurant(self):
#         print('Restauant Name: ',self.restaurant_name)
#         print('Cuisine_type: ',self.cuisine_type)

#     def open_restaurant(self):
#         print(self.restaurant_name, 'is now open!')

# restaurant = Restaurant('Chicken Tonight, Nankulabye', 'Take Away')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()



#EVENING SESSION
#OOP CONCEPTS
#ENCAPSULATION, ABSTRACTION, INHERITANCE, POLYMORPHISM
#what is encapsulation? It is a process of wrapping attributes and methods in a single unit called a class
#why encapsulation? prevents direct access to data. controls access of variables. impoves code maintainability
#Real world example

#example 1
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# student1 = Student('sarah', 29)
# print(student1.age)
# print(student1.name)

#Acess modifiers
#python supports 3 access modifiers
#public (accessible everywhwere), protected(accessible within the class and subclass), private(accessible only inside the class)

#example
#Employee
# class Employee:
#     def __init__(self):
#         self.name = 'Peter'
#         self._salary = 600000       #_ means protected, __means private

# emp = Employee()
# print(emp.name)
# print(emp._salary)

    
#exercise one
#create a class called car with brand,model,pricethen make brand public, model protected, price private, display all values appropriately

# class Car:
#     def __init__(self):
#         self.brand = 'Toyota'
#         self._model = 'T1'
#         self.__price = 20000000

# car = Car()
# print(car.brand)
# print(car._model)
#print(Car.__price)


#Data Hiding
#Real world bank account
# class BankAccount:
#     def __init__(self):
#         self.__balance = 1000000

#     def deposit(self, amount):
        # self.__balance += amount              #it brings an error

#     def show_balance(self):
#         return self.__balance + self.deposit
    
# acc = BankAccount()
# acc.deposit = (500000)
# print(acc.show_balance())


#exercise: create a class called MobileMoney. it should show balance, enable deposit and withdraw
# class MobileMoney:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"UGX {amount: } deposited successfully.")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"UGX {amount:,} withdrawn successfully.")
#         else:
#             print("Insufficient balance!")

#     def check_balance(self):
#         print(f"Current Balance: UGX {self.__balance:,}")

# acc =MobileMoney()
# acc.deposit(3000000)
# acc.withdraw(345000)
# acc.check_balance()


#Abstraction
#what is Abstraction? it hides implementation details and displays only important data

#Lab activity 2
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         print('Car started')
#     @abstractmethod
#     def stop(self):
#          print('car stopped')

# car = Vehicle()

# car.start()
# car.stop()

#inheritance
#what is inheritance? 
#parent/ super /base class
#child/ sub/ derived class

class Person:

    def display(self,name):
        self.name = name
        print('Name:', self.name)

