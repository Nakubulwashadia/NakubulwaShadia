# 26-06-2026
# MORNING SESSION
# FILE HANDLING IN PYTHON
'''
mode               Meaning

'''

#Example 1 Read a student.txt file
# file = open("student.txt", "r")

# content = file.read()

# print(content)
# file.close()

#Recommended method
#'with' automatically closes the file

# with open('student.txt', 'r') as file:
#     data = file.read()

# print(data)

#reading line by line
# with open('student.txt', 'r') as file:
#     for line in file:
#         print(line.strip())


#Lab Exercise 1: write a file with the contnt 'i love python programming'. 
# 'I am becoming a data scientist', second line. save your file as report.txt

# with open('report.txt', 'w') as file:
#     file.write('I love python programming.\n')
#     file.write('I am becoming a data scientist')

#Appending a file, use the sample report.txt append 'Everydata scientist must learn python'

# with open('report.txt', 'a') as file:
#     file.write("\nEverydata scientist must learn python")

#Real world example
#Attendance system
#Live demo

# name = input('Enter Student: ')
# with open('attendance.txt', 'a') as file:         #not complete
#     file.write(name + '\n')



#working with CSV file
#what is csv? comma separated values

# import csv


#JSON PROCESSING
# JSON format
# {
#   "name": "Rinah",
#   "age" : 28
# }

#writing a json file
# import json

# student = {
#     "name": "Jeff",
#     "Age": "22",
#     "Course": "python"
# }

# with open('student.json', 'w') as file:
#     json.dump(student,file,indent=4)

# print('JSON file created successfully')


# import json

# with open('student.json', 'r') as file:
#     student = json.load(file)
# print(student)


#EXCEPTION HANDLING
# an exception is an error that occurs during code running

#examples
'''
Division by zero
file not found
invalid input
invalide input
index out of range
'''

#code, try, catch, finally

#try block



#finally block: executes whether an error occurs or not
#reading a file
# try:
#     file = open('student.json')
#     print(file.read())

# except FileNotFoundError:
#     print('file missing')

# finally:
#     print('Finished opening')


#Real world example
#ATM withdrawal

# class InsufficientBalance(Exception):
#     pass

# balance = 2000000
# withdraw = int(input('Amount: '))

# try:
#     if withdraw > balance:
#         raise InsufficientBalance('Insufficient Funds')
    
#     balance -= withdraw

#     print('Remaining Balance: ', balance)

# except InsufficientBalance as error:
#     print(error)


## Debugging
# what is debugging? is a process of finding and fixing program errors

'''
commmon errors
-syntax errors
-runtime errors
-logical errors
'''

#Example 4:

# marks = 70

# if marks = 70:
#     print('A')

#correct version of the syntax

number = [2, 4, 6, 8, 10]

# print('current list: ', number)

# for n in number:
#     print('current number: ', n)


import logging
logging.basicConfig(
    filename = 'system.log',
    level=logging.INFO
)

logging.info('Application started')
logging.warning('low memory')
logging.error('Database connection Failed')


