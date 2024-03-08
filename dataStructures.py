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
mySet = {1, 4, 1, 5, 9}
print("set: ", mySet)