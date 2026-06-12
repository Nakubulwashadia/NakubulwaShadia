# 10th - 06-2026
# DAY TWO
#MORNING SESSION

#OPERATORS
#PRECEDENCE AND ASSOCIATIVITY
#a = 20
#b = 30
#c =10

#print(a + b * c) # 20 + 300 = 320
#print((a + b) * c) # 50 * 10 = 500
#print((b-c)*((a+c)/(a-c))) # 20 * (30/10) = 60


#IF STATEMENT
#cars = ['audi', 'bmw', 'subaru', 'toyota']

#for car in cars:

#    if car =='toyota':
#       print(car.upper())
        
#    else:

#       print(car.title())


#CONDITIONAL TESTS
#car = 'SUBARU'
#print("Is car == 'subaru'?")
#print(car == 'Subaru')
#print(car.lower() )



#CHECKING FOR INEQUALITY
#requested_topping = 'mushrooms'
#if requested_topping != 'pepperoni':
#    print("Hold the pepperoni!")

#EXAMPLE 2
#toppings = ['mushrooms', 'olives', 'pepperoni']

#for topping in toppings:
#    if topping != 'olives':
#        print("not olives")
#    else:
#        print('olives')


#CHECKING MULTIPLE CONDITIONS
#single= True
#age_1 = 18
#if single and age_1 >= 21:
#    print("You are 21 and not married when older.")
#else:
#    print("You are young enough.")


#CHECKING WHETHER A VALUE IS IN A LIST
#requested_toppings = ['mushrooms', 'onions', 'pineapple']
#print('mushrooms' in requested_toppings)
#print('pepperoni'  not in requested_toppings)


#CHECKING WHETHER A VALUE IS NOT IN A LIST
#banned_users = ['andrew', 'carolina', 'david']
#user = 'david'
#if user not in banned_users:
#    print(f"{user.title()}, you can post a response if you wish.")
#else:
#    print(f"{user.title()}, you are banned from posting a response.")


#BOOLEANS
#A = 10
#B = 20
#print(A==B) # False

#EXAMPLE 2
# var1 = 0
# var2 = 2
# var3 = -9.99
# var4 = ""
# print(bool(var1)) # False
# print(bool(var2)) # True
# print(bool(var3)) # True
# print(bool(var4)) # False


#EVENING SESSION
#CONTROL STRUCTURES
#CONDITIONAL STATEMENTS

# x = int (input("Enter a number: "))
# if x > 0:
#     print(" X is a Positive number")
# elif x == 0:
#     print(" X is Zero")
# else:
#     print(" X is a Negative number")
    
# GRADING SYSTEM
# score = int(input("Enter your score: "))
# if score >= 90:
#         print("Grade: A")
#         message = "Congratulations! You scored an A."
# elif score >= 80:
#         print("Grade: B")
#         message = "Great job! You scored a B."
# elif score >= 70:
#         print("Grade: C")
#         message = "Good effort! You scored a C."
# elif score >= 60:
#         print("Grade: D")
#         message = "You passed! You scored a D."
# else:
#         print("Grade: F")
#         message = "Sorry, you failed."
# print(message)


#SWITCH CASE STATEMENT
# grade = input("Enter your grade (A, B, C, D, F): ")
# match grade:
#     case 'A':
#         print("Grade: A")
#         message = "Congratulations! You scored an A."
#     case 'B':
#         print("Grade: B")
#         message = "Great job! You scored a B."
#     case 'C':
#         print("Grade: C")
#         message = "Good effort! You scored a C."
#     case 'D':
#         print("Grade: D")
#         message = "You passed! You scored a D."
#     case 'F':
#         print("Grade: F")
#         message = "Sorry, you failed."
#     case _:
#         print("Invalid grade. Please enter a valid grade (A, B, C, D, F).")
# print(message)

#Exe 1
# day = int(input("Enter a number for a day: "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid input. Please enter a number between 1 and 7.")

#NESTED IF STATEMENT
users = {
    "user1": {"username": "john_doe", "password": "password123", "role": "admin"},
    "user2": {"username": "jane_smith", "password": "securepass456", "role": "user"},
}

# if "username" in users["user1"] and "password" in users["user1"]:
#     if users["user1"]["username"] == "john_doe" and users["user1"]["password"] == "password123":
#         print("Login successful! Welcome, admin.")
#     else:
#         print("Invalid username or password for user1.")

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if user in users:
#     if users[user]["username"] == username and users[user]["password"] == password:
#         print(f"Login successful! Welcome, {users[user]['role']}.")
#     else:
#         print("Invalid username or password.")

#         if users[user]["role"] == "admin":
#             print("You have admin privileges.")
#         else:
#             print("You have user privileges.")


#Login authentication system