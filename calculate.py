# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 08:42:25 2023

@author: hemalatha
"""

def sum(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def mul(a,b):
    return a*b;
def div(a,b):
    return a/b;
def rem(a,b):
    return a//b;
print("1.Addition");
print("2.Subtraction")
print("3.Multiplication");
print("4.Division")
print("5.Remainder")
try:
    choice = int(input("Enter the choice: "))
    if choice not in [1, 2, 3, 4, 5]:
        raise ValueError("Invalid choice! Please enter a number between 1 and 5.")
    
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))

    if choice == 1:
        result = sum(a, b)
        print(f"The sum is {result}")
    elif choice == 2:
        result = sub(a, b)
        print(f"The subtraction is {result}")
    elif choice == 3:
        result = mul(a, b)
        print(f"The multiplication is {result}")
    elif choice == 4:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = div(a, b)
        print(f"The division is {result}")
    elif choice == 5:
        result = rem(a, b)
        print(f"The remainder is {result}")

except ValueError as e:
    print(f"Error: {e}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
