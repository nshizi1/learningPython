#  There are 2 types pf functions:
#     1. Built-in functions that came with python program
#     2. User-defined functions, those that are created during ContentTransferEncoding
    
    # 1. Use some of the built-in functions
print("Hello python program")
# input("Enter your names: ")
numbers = {1,3,1,8}
print(sum(numbers))
name = "Wilson"
print(len(name))
print(len(numbers))
print(type(numbers))
print(sorted(numbers))
print(max(numbers))
print(min(numbers))
print(abs(-21))
number = "123"      #datatype is string
print(int(number))
print(type(int(number)))    #datatype is integer
    # 2. Use some of the user-defined functions
def name():
    print("Hello functions")
name()

def add(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1+num2}")

add(2, 3)
