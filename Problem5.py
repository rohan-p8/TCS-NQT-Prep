"""
Write a program to reverse the digits of a given number.
"""
"""
2. Logic

The idea is simple:

-Take the last digit of the number.
-Add it to a new number.
-Remove the last digit from the original number.
-Repeat until the original number becomes 0.
"""

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    last_digit = n % 10
    reverse = (reverse * 10) + last_digit
    n = n // 10


print("Reversed number:", reverse)
