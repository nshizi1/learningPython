# lists, tuple, sets, dictionaries
# lists
myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(myList)
# lists methods
myList.append(4)
print(myList)
myList.extend([5, 7])
print(myList)
myList.insert(0, 9)
print(myList)
myList.remove(4)
print(myList)
myList.pop(6)
print(myList)
myList.index(9)
myList.append(9)
print(myList)    
print(myList.count(9))      #outputs 2 coz 9 comes twice in the list
myList.sort()
print(myList)
myList.reverse()
print(myList)


# tuple: they can not be changed after creation

myTuple = (1, 2, 3, 4, 5)
print("tuple: ", myTuple)
print(myTuple[3])   # 4
# myTuple.append(3)   #generate error


# sets

# mySet = set(myTuple)    #will have values of the tuple
# mySet = set([1, 4, 1, 5, 9])  #this can also work
mySet = {1, 4, 1, 5, 9, 1, 3}
print("set: ", mySet)
mySet.add(3) 
# Note that a value can be only added once
print("set: ", mySet)   #output is :{1, 3, 4, 5, 9}  #One is used once
mySet.remove(1) 
print(mySet)    #All ones are removed


# Dictionaries: set of key-value pairs

# Syntax: dictionaryName = {key1: value1, key2: value2, ...}

myDict = {"name": "Wilson", "age": 23, "address": "Kigali"}
print(myDict["name"])   #Outputs WIlson
print(myDict)   #prints all the data in a dictionary    
# Adding new value to dictionary
myDict["Hobby"] = "Cooking"
print(myDict["Hobby"])      #Outputs Cooking
# updating value of key
myDict["age"] = 18
print(myDict["age"])    #now outputs 18

# removing keys
del myDict["address"]
# print(myDict["address"]) #Will generate error message coz key is deleted
print(myDict)
# Dictionary methods
print(myDict.keys())    #outputs keys only: name, age, hobby
print(myDict.values()) #outputs values only: Wilson, 18, Cooking
print(myDict.items())   #outputs keys & values pairs as tuple: ([('name', 'Wilson'), ('age', 18), ('Hobby', 'Cooking')])
if "name" in myDict:    #checking existence of keys
    print(f"Key exists with value {myDict['name']}")
else:
    print("Key does not exist")

# nested dictionary
nestDict = {"names": {
    "first name": "Wilson",
    "last name": "Nshizirungu"},
            "age": 23,
            "address": "Kigali"}
# display first and last names
print(nestDict["names"])
# first name only
print(nestDict["names"]["first name"])
if "first name" in nestDict:
    print(f"Key exists with value {nestDict['names']['first name']}")
else:
    print("Key does not exist")
# the above will fail coz key : "first name" is in "name", do the following instead
    
if "first name" in nestDict["names"]:
    print(f"Key exists with value {nestDict['names']['first name']}")
else:
    print("Key does not exist")

# checking if names exists in the dictionary    
if "names" in nestDict:
    print(f"Key exists with value {nestDict['names']}")
else:
    print("Key does not exist")
    
people = {
    "person": {
        "names": {
            "firstName": "Kevin",
            "lastName": "Mitchell"
        }
    }
}
if "firstName" in people["person"]:
    print(f"Key exists with value {people['person']['names']['first name']}")
else:
    print("Key does not exist")