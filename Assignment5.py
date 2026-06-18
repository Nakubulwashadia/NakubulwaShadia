
#     DATA STRUCTURES PRACTICE ASSIGNMENT

#           EXERCISE 1 - LISTS


# print("\n===== EXERCISE 1: LISTS =====")

# 1. Create a list with 5 names and output the 2nd item
# names = ["Shadia", "Rinah", "Brian", "Joel", "Mercy"]
# print("1.", names[1])

# 2. Change the first item to a new value
# names[0] = "Nakubulwa"
# print("2.", names)

# 3. Add a sixth item
# names.append("Sandra")
# print("3.", names)

#  4. Add "Bathel" as the 3rd item
# names.insert(2, "Bathel")
# print("4.", names)

# # 5. Remove the 4th item
# names.pop(3)
# print("5.", names)

# 6. Negative indexing to print last item
# print("6.", names[-1])

# 7. New list of 7 items, print 3rd, 4th and 5th
# fruits = ["mango", "banana", "apple", "orange", "grape", "pineapple", "pawpaw"]
# print("7.", fruits[2:5])

# 8. List of countries and make a copy
# countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Ethiopia"]
# countries_copy = countries.copy()
# print("8. Original:", countries)
# print("   Copy:", countries_copy)

# 9. Loop through list of countries
# print("9. Looping through countries:")
# for country in countries:
#     print("  ", country)

# 10. List of animals sorted ascending and descending
# animals = ["zebra", "lion", "elephant", "antelope", "buffalo", "giraffe"]
# animals.sort()
# print("10. Ascending:", animals)
# animals.sort(reverse=True)
# print("    Descending:", animals)

# 11. Output only animal names with letter 'a'
# print("11. Animals with 'a':")
# for animal in animals:
#     if "a" in animal:
#         print("  ", animal)

# 12. Join two lists of first and second names
# first_names = ["Shadia", "Rinah", "Brian"]
# second_names = ["Nakubulwa", "Atuhaire", "Mugisha"]
# full_names = first_names + second_names
# print("12.", full_names)


#           EXERCISE 2 - TUPLES


# print("\n===== EXERCISE 2: TUPLES =====")

# 1. Output favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
# print("1.", x[2])  # tecno is favorite

# 2. Negative indexing to print 2nd last item
# print("2.", x[-2])

# 3. Update "iphone" to "itel"
# y = list(x)
# y[1] = "itel"
# x = tuple(y)
# print("3.", x)

# 4. Add "Huawei" to tuple
# x = list(x)
# x.append("Huawei")
# x = tuple(x)
# print("4.", x)

# 5. Loop through tuple
# print("5. Looping through phones:")
# for phone in x:
#     print("  ", phone)

# 6. Remove first item from tuple
# x = list(x)
# x.pop(0)
# x = tuple(x)
# print("6.", x)

# 7. Tuple of cities in Uganda using tuple() constructor
# cities = tuple(("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu", "Mbale"))
# print("7.", cities)

# 8. Unpack the tuple
# city1, city2, city3, city4, city5, city6 = cities
# print("8. Unpacked:", city1, city2, city3, city4, city5, city6)

# 9. Print 2nd, 3rd and 4th cities using range of indexes
# print("9.", cities[1:4])

# 10. Join two tuples of first and second names
# first = ("Shadia", "Rinah", "Brian")
# second = ("Nakubulwa", "Atuhaire", "Mugisha")
# joined = first + second
# print("10.", joined)

# 11. Create a tuple of colors and multiply by 3
# colors = ("red", "blue", "green")
# print("11.", colors * 3)

# 12. Return number of times 8 appears
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# print("12.", thistuple.count(8))



#           EXERCISE 3 - SETS

# print("\n===== EXERCISE 3: SETS =====")

# 1. Create a set of beverages using set() constructor
# beverages = set(("juice", "tea", "coffee"))
# print("1.", beverages)

# 2. Add 2 more items to beverages set
# beverages.add("water")
# beverages.add("milk")
# print("2.", beverages)

# 3. Check if microwave is in the set
# mySet = {"oven", "kettle", "microwave", "refrigerator"}
# print("3. microwave in set:", "microwave" in mySet)

# 4. Remove kettle from the set
# mySet.remove("kettle")
# print("4.", mySet)

# 5. Loop through the set
# print("5. Looping through set:")
# for item in mySet:
#     print("  ", item)

# 6. Add list elements to a set
# my_set = {"pen", "book", "ruler", "bag"}
# my_list = ["pencil", "eraser"]
# my_set.update(my_list)
# print("6.", my_set)

# 7. Join two sets of ages and first names
# ages = {23, 21, 25, 22}
# f_names = {"Shadia", "Rinah", "Brian"}
# joined_set = ages.union(f_names)
# print("7.", joined_set)



#           EXERCISE 4 - STRINGS

# print("\n===== EXERCISE 4: STRINGS =====")

# 1. Concatenate integer and string
# age = 34
# name = "Shadia"
# print("1.", name + " is " + str(age) + " years old")

# 2. Remove spaces at beginning, middle and end
# txt = "      Hello,       Uganda!       "
# clean = txt.strip().replace("       ", " ")
# print("2.", clean)

# 3. Convert to uppercase
# print("3.", txt.upper())

# 4. Replace 'U' with 'V'
# print("4.", txt.replace("U", "V"))

# 5. Return characters in 2nd, 3rd and 4th position
# y = "I am proudly Ugandan"
# print("5.", y[1:4])

# 6. Fix the string with quotes inside
# x = 'All "Data Scientists" are cool!'
# print("6.", x)




#         EXERCISE 5 - DICTIONARIES


# print("\n===== EXERCISE 5: DICTIONARIES =====")

# Shoes = {
#     "brand": "Nike",
#     "color": "black",
#     "size": 40
# }

# 1. Print shoe size
# print("1. Shoe size:", Shoes["size"])

# 2. Change "Nike" to "Adidas"
# Shoes["brand"] = "Adidas"
# print("2.", Shoes)

# 3. Add "type": "sneakers"
# Shoes["type"] = "sneakers"
# print("3.", Shoes)

# 4. Return list of all keys
# print("4. Keys:", list(Shoes.keys()))

# 5. Return list of all values
# print("5. Values:", list(Shoes.values()))

# 6. Check if key "size" exists
# print("6. 'size' exists:", "size" in Shoes)

# 7. Loop through dictionary
# print("7. Looping through dictionary:")
# for key, value in Shoes.items():
#     print(f"   {key} : {value}")

# 8. Remove "color"
# Shoes.pop("color")
# print("8.", Shoes)

# 9. Empty the dictionary
# Shoes.clear()
# print("9.", Shoes)

# 10. Create a dictionary and make a copy
# person = {"name": "Shadia", "age": 56, "city": "Kampala"}
# person_copy = person.copy()
# print("10. Original:", person)
# print("    Copy:", person_copy)

# 11. Nested dictionaries
students = {
    "student1": {
        "name": "Shadia",
        "age": 56,
        "city": "Kampala"
    },
    "student2": {
        "name": "Rinah",
        "age": 29,
        "city": "Entebbe"
    },
    "student3": {
        "name": "Brian",
        "age": 35,
        "city": "Jinja"
    }
}
print("11.", students)