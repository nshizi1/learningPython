# Conditional statement: if,  if-else, if-elif-else, and nested if

age = 23
if age < 18:
    print("You are not old enough to vote.")
elif age > 50:
    print("You are too old to vote.")
else:
    print("You are allowed to vote")
    
# The above can have if, if-else and if-elif-else statements
# nested if-else statements

a = 0
b = 3
c = 1
if a > b:
    if a> c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b > c:
        print("B is greatest")
else:
    print("C is greatest")
 
# if like switch case

def week(number):
    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")
    else:
        print("Invalid day")

    
day  = int(input("Enter day number you want to display: "))

week(day)
