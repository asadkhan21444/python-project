import math
def num(numer):
    return numer **2 


res = num(3)
res = num(4)
print(res)

# ------------------------------

#  two peramiter add

def add(num1,num2):
    return num1 + num2

res = add(2,1)
print(res)

# ----------------------- 
# multiply two number or number and string

def mul(a1,a2):
    return a1*a2


print(mul(4,5))
print(mul(4,"a"))
print(mul("b",5))


# ...................................
# area of circumference and redus
def circle_status(radius):
    area = 2 * math.pi * radius
    circumference = 2 * math.pi * radius
    return area, circumference 

print(circle_status(2))

    # ---------------------------------------

def greet(name= "User"):
    return "hello," + name + "!"

print(greet("chai"))
print(greet())

# ------------------------------------
# lambda

cube = lambda x: x ** 3          # x is perameter

print(cube(4))
# .....................................

# *args

def sum_all(*args):
    # print(args)
    return (args)
    # for i in args:
    #     print(i * 2)


print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5,6,7,8))
print(sum_all(1,2,3,4,5,6,7,8,9,10))



# project in function

# Simple Calculator using Python Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("Invalid input!")

# Run the calculator
calculator()



# .///////////////////////////////////////////

import random, string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    length = int(input("Enter password length: "))
    print("Your new password:", generate_password(length))


main()