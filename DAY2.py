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
var1 = 0
var2 = 2
var3 = -9.99
var4 = ""
print(bool(var1)) # False
print(bool(var2)) # True
print(bool(var3)) # True
print(bool(var4)) # False