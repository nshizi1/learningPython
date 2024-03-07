# 1. Arithmetic
# 2. Comparison
# 3. Logical
# 4. Assignment
# 5. Membership
# 6. Identity
# 7. Bitwise

# arithmetic operators

# + - / * %

a = 5
b=8
c = a-b
print(a-b)
print(c)
print(f"In Subtraction,{a}-{b} is {c}")
print(f"In Addition,{a}+{b} is {a+b}")
print(f"In Multiplication,{a}*{b} is {a*b}")
print(f"In Division,{b}/{a} is {b/a}")
print(f"In Floor division,{b}//{a} is {b//a}")
print(f"The modulus of {b} to {a} is {b%a}")
print(f"The exponential of {b} to {a} is {b**a}")
print(f"The exponential of 3 to 2 is {3**2}")   # means 3 on the exponent of 2 which equals 9. 3 power 2

# Comparison operators

a = 3
b = 9
if a == b:
    print("a is equal to b")
else:
     print("a is greater than b")

if a != b:
    print("a is not equal to b")
else:
    print("a is equal b")
    
if a < b:
    print("a is smaller than b")
else:
    print("a is greater than b")
    
# other comparison operators are not implemented like: >, <=, >=

# logical operator: and, or, not
a = 5
b = 8
if a == 5 and b == 8:
    print("both values are true")
else:
    print("all values are not true")
if a == 3 or b == 4:
    print("at least one value is true")
else:
    print("no value is true")
if not a == 4:
    print("a is not equal to 4")
    
# assignment operators: +=, -=, *=, /=, %=, **=, //=, **=

# membership operators: in, not in

numbers = {1, 2, 3, 6}
if 5 in numbers:
    print("5 is in numbers")
else:
    print("5 is not in numbers")
    
if 2 not in numbers:
    print("2 is not in numbers")
else:
    print("2 is in numbers")
    
# identity operators: is, is not

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False (different objects)
print(a is not b)  # True (different objects)
print(a is c)      # True (same object)
print(a is a)

# Bitwise operators

x = 5  # binary representation: 0b101
y = 3  # binary representation: 0b011

print(x & y)   # Bitwise AND: 0b001 (decimal 1)
print(x | y)   # Bitwise OR:  0b111 (decimal 7)
print(x ^ y)   # Bitwise XOR: 0b110 (decimal 6)
print(~x)      # Bitwise NOT: -6 (complement of 5)
print(x << 1)  # Left Shift:  0b1010 (decimal 10)
print(x >> 1)  # Right Shift: 0b10 (decimal 2)
