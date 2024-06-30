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
print("1.addition");
print("2.subtraction")
print("3.multiplication");
print("4.division")
print("5.remainder")
choice=eval(input("enter the choice"));
a=int(input("enter the fisrt value:"));
b=int(input("enter the second value:"));
if(choice==1):
    c=sum(a,b);
    print("the sum is", c);
elif(choice==2):
    c=sub(a,b)
    print("the subtraction is",c);
elif(choice==3):
    c=mul(a,b)
    print("the multiplication is",c);
elif(choice==4):
    c=div(a,b);
    print("the division is",c);
elif(choice==52):
    c=rem(a,b);
    
    print("teh remainder is", c);
else:
    print("INVALID INPUT")
