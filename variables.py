number = 5
print(number)
floatPoint = 5.5
print(floatPoint)
names = "Wilson Nshizirungu"
print(names)
# Concatenating Strings
fName = "Wilson"
lName = "Nshizirungu"
fullName = fName+" "+lName
print(fullName)
fruits = ["mango", "banana", "orange", "apple"]
for fruit in fruits:
    print(fruit)
foods = ("meat", "rice", "beans", "maize")
for food in foods:
    print(food)
person = {"name": "Wilson",
          "age": 25,
          "city": "Kigali"}
for key, value in person.items():
    print(key,": ",value ) #this method
    print(f"{key}: {value}") #or this one