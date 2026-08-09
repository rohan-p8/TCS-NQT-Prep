"""
Question 3: Factorial of a Number
"""

"""
The factorial of a number n means multiplying all positive integers 
from 1 to n.
"""

n = int(input("Enter a number: "))

fact =1

for i in range(1, n + 1):
    fact = fact * i

print(f"The factorial of {n} is: {fact}")