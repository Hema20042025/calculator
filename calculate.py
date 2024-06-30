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
choice=eval(input("Enter the choice"));
a=int(input("Enter the fisrt value:"));
b=int(input("Enter the second value:"));
if(choice==1):
    c=sum(a,b);
    print("The sum is", c);
elif(choice==2):
    c=sub(a,b)
    print("The subtraction is",c);
elif(choice==3):
    c=mul(a,b)
    print("The multiplication is",c);
elif(choice==4):
    c=div(a,b);
    print("The division is",c);
elif(choice==52):
    c=rem(a,b);
    
    print("The remainder is", c);
else:
    print("INVALID INPUT")
