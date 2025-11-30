# python program to create a simple calculator

#    3 steps to create a simple calculator

#    1. functions for operations
#    2.  take user input
#    3.  display result

#     functions to add two nimbers

def add(num1, num2):
    return num1 + num2

#   functions to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

#  functions to multiply two  nimbers
def multiply(num1, num2):
    return num1 * num2

#  functions to divide two  numbers
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by xero"
    else:
        return num1 / num2
    
# function for average of two numbers
def average(num1, num2):
    return (num1 + num2) / 2

    
#  take user input
print("Please Selcet opertion:\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. multiplication\n"\
      "4. divide\n" \
      "5. average\n" 
      )

choice = input("Enter choice (1/2/3/4/5):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter secound number: "))

# display result
if choice == '1':
    print(f"The addition of Two numbers is: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"The Subtraction of Two numbers is: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"The multiplication of Two numbers is: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"The  Division of Two numbers is: {num1} / {num2} = {divide(num1, num2)}")

elif choice == '5':
    print(f"average of {num1} and {num2} = {average(num1, num2)}")
else:
    print("Invalid input")

# ///////////////////////////////////////////////////////////////////////////////////////////


          
