#24-06-2026
#MORNING SESSION
#INHERITANCE
#It's inheriting attributes and methods fromanother class (parent or base class)
#Benefits of inheritance
#1- supports method overriding, 2- promotes code reusability  3- models real world scenarios  4- central mgt at parent level 6- also supports scalable designs using polymorphism
#example 1
# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def info(self):
#         print('Animal name:',self.name)

# #create a child class
# class Dog(Animal):
#     def sound(self):
#         print(self.name, 'barks')

# w = Dog('Buddy')
# #inherited method
# w.info()
# w.sound()


#Super() fuction
#this is used to call methods from a super class using MRO(Method Resolution Order)
#used in the child class

#example2
# class Animal:
#     def __init__(self,name):
#         self.name = name
       
#     def info(self):
#         print('Animal name:',self.name)

#create a child class
# class Dog(Animal):
#     def __init__(self,name,breed):
#         self.breed =breed
#         super().__init__(name)

#     def details(self):
#         print(self.name, 'is a', self.breed)

# z = Dog('Buddy', 'German Shephard')
# #inherited method
# z.info()
# z.details()
        

#METHOD OVERRIDING
#allows a child to provide it's own implementation of a method that already exists in the parent class
# class Animal:
#     def sound(self):
#         print('Animal sounds')

# class Dog(Animal):
#     def sound(self):
#         print('a Dog Barks')

# s = Dog()
# s.sound()

# when a class inherits fron more than one class
#Diamond problem - occurs whhen two classes inherit fron a common superclass and another class inherits from both of them
#if a method is overridden in the immediate classes, ambiquity arises about which method the derived class should 
#Method Resolution Order - determines the order in which the base classes are searched when looking for an attribute
# it follows linearization rule

# class   A:
#     def w(self):
#         print('from A')

# class B(A):
#     def w(self):
#         print('from B')

# class C(A):
#     def w(self):
#         print('from C')

# class D(B,C):
#     pass
# obj = D()
# obj.w()
# print(D.__mro__)


#EVENING SESSION
#Polymorphism
#it is multiple methods but different parameters
# why polymorphism?
'''
-Default parameters
-Variables length arguments(*kwargs, arg)
-Type checking within a single method (checking the data type)

'''

#Example 1
#in Java

# class Calculator{
#     int add(int a, int b)
#     int add(int a, int b, int c)
# }


# In python
#Method Overloading
#Approach 1: Default parameters

# class Calculator:
#     def add(self, a, b, c):
#         return a + b + c
    
#Approach 2: Variable length Arguments
# class Calculator:
#     def add(self, *args):
#         if len(args) == 2:
#             return args[0] + args[1]
        
#         elif len(args) == 3:
#             return args[0] + args[1] + args[3]
        
#         else:
#             return 0
        
# Approach 3: Type checking
# class Calculator:
#     def add(self, a, b):
#             return a + b
#         if isinstance(a, int) and isinstance(b, int):
#             return float(a) + float(b)
    
#Method overriding
'''
the method signature(name and parameter) must match
super() allow calling the parent method
overriding enable dynamic behaviors at return
'''
# real world WEExample: Bank Account

class BankAccount:
    def calculate_interest(self, balance, rate):
        return balance * rate/100
    
    def get_account_type(self):
        return 'Generic Bank Account'
    
class SavingAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        monthly_rate = rate/ 12 /100
        return balance * ((1 + monthly_rate)**12-1)
    
    def get_account_type(self):
        return 'Saving Account'
    
class CurrentAccount(BankAccount):
    def calculate_interest(self, balance, rate):
        return super().calculate_interest(balance, rate)
    
    def get_account_type(self):
        return 'Checking Account'

#Exercise : Create a method overloading and overriding the completes a banking system
# The parent class must be transaction and the child class can be deposit, withdrawal and transfer.
#Demonstrate an employer depositing, withdrawing and transferring funds.

# Operator overloading 
'''
- Add +, subtract -, Multiply *, division /
common specicial methods:
__add__()
__sub__(self,other)
__mul__(self,other)
__truediv__(self, other)
__str__(self, other)
'''

#Example 3
class Money:
    def __init(self, amount, currency='UGX'):
        self.amount + amount
        self.currency + currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueErrror('Cannot add different currencies')
        

#Automation and webscrapping
#what is automation in python?
'''
The Automation pipeline:
Input ->, Transform ->, Output ->, Reliability -> Run

#Key libraries for Automation
Library
pathlib - file path
shutil - copy, move, archive
Schedule - task Scheduling
Watchdog - file System events monitoring
openpyxl - Excel file read / write
'''

#FILE AUTOMATION
# Organising files on our computer

#Example 4
#Get the file path downloads
#file path
#Approach : pathlib
from pathlib import Path
file_path = Path.home() / "Downloads" / "report.pdf"


#File organisation script
# real world we can automatically organised a download folder by file type

#Import libraries
from pathlib import Path
import shutil
from datetime import datetime
from dataclasses import dataclass

#-- Configuration
@dataclass(frozen=True)
class Config:
    source_dir: Path
    destination_dir: Path
    dry_run: bool = True

EXTENSION_MAP = {
    'Images': [".jpg", "jpeg", ".png", ".svg"],
    'Documents': [".pdf", ".docx", ".txt"],
    'Videos': [".mp4", ".mkv", "mov"],
    'Code': [".py", ".js", ".html"],
    'Archives': [".zip", ".tar", ".gz"],
}

#Assignment
#code logic for file automation

# web scraping
#automated way of extracting data from web sites using python scripts

