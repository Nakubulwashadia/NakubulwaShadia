                 #DAY ONE 8th- 06- 2026
                 #EVENING SESSION

                 #STARTER CODE

#total = 0
#count = 0

#while count < 5:
#    num = float(input("Enter a number: "))
#    total = total + num
#    count = count + 1

#average = total / 5
#print("The average is: ", average)


           #INPUT FUNCTION
#age = int(input("Enter your age: "))
#if age >=18:
#    print("You are an adult.")
#else:
#   print("You are a minor.")


           #OUTPUT OPERATION
#print ("i love python programming")


           #FORMATTED STRINGS
#name = 'Shadia'
#age = 20
#height = 1.65
#print(f"My name is {name}, I am {age} years old and my height is {height} meters.")

#AREA
#length = float(input("Enter the length of the rectangle: "))
#width = float(input("Enter the width of the rectangle: "))
#area = length * width
#print(f"The area of the rectangle is: {area:.2f}cm²")


         #ESCAPE SEQUENCE
#name = 'Shadia'
#age = 20
#height = 1.65
#print(f"My name is {name} \nI am {age} years old \nMy height is {height} meters. \n\"Hi there!\"")


          #EXERCISE
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#birth_year = int(input("Enter your birth year: "))
#city = input("Enter your city: ")

#age = 2026 - birth_year

#print(f"\nHello! My name is {first_name} {last_name}.\nI am {age} years old.\nI live in {city}.")


         #EXERCISE 2
secret_number = int(input("Enter your secret number: "))

for attempt in range(3):
    guess = int(input(f"Attempt {attempt + 1}: Guess the number: "))
    if guess == secret_number:
        print(f"\n✅ CORRECT! The number was {secret_number:,}")
        break
else:
    print(f"\n❌ Out of attempts! The secret number was {secret_number:,}")