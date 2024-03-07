number = 5  #integer
print(number)
floatPoint = 5.5    #float point
print(floatPoint)
names = "Wilson Nshizirungu"    #string
print(names)
# Concatenating Strings
fName = "Wilson"
lName = "Nshizirungu"
fullName = fName+" "+lName
print(fullName)
fruits = ["mango", "banana", "orange", "apple"]     #list
for fruit in fruits:
    print(fruit)
foods = ("meat", "rice", "beans", "maize")      #tuple
for food in foods:
    print(food)
person = {"name": "Wilson",
          "age": 25,
          "city": "Kigali"}     #dictionary
for key, value in person.items():
    print(key,": ",value ) #this method
    print(f"{key}: {value}") #or this one

null = None #None datatype, same as the null datatype
print(null)

numbers = {1,2,3}   #set datatype
for number in numbers:
    print(number)