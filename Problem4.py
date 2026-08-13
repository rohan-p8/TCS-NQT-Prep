"""
Question 4: Fibonacci Series
"""
"""
In the Fibonacci series, every new number is the sum of the 
previous two numbers. 
"""
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    