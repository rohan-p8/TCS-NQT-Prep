"""
Problem Statement

Write a program that checks whether a given number is:

Even, or
Odd
"""

a = int(input("Enter a number: "))

if a % 2 == 0:
    print(f"{a} is an Even number.")
else:
    print(f"{a} is an Odd number.")