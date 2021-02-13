# !/bin/python3
"""
www.hackerrank.com/challenges/input
You are given a polynomial P of a single indeterminate (or variable) x.
You are also given the values of x and k. Your task is to verify if P(x)=k

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
x = 1
k = 4
polynomial = 'x**3 + x**2 + x + 1'
print(eval(polynomial) == k)
