"""
Write a program to check whether a given number is Prime or Not Prime.
"""

"""
A prime number is number that has only two factors, 1 and itself. 


"""
import math


n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not a prime number")
else:
    is_prime = True


    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number ")
        