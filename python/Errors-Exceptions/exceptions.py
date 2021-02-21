"""
https://www.hackerrank.com/challenges/exceptions/problem
github.com/ander758/HackerRank

You are given two values a and b.
Perform integer division and print a/b.
"""

arr = ['3', '1 0', '2 $', '3 1']
for element in arr[1:]:
    try:
        args = [int(arg) for arg in element.split(' ')]
        print(round(args[0]//args[1]))
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')
    except ValueError as e:
        print(f'Error Code: {e}')
