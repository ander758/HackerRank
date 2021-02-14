"""
www.hackerrank.com/challenges/any-or-all
github.com/ander758/HackerRank

Check if all are positive and if any int is palindrome
"""

arr = ['12', '9', '61', '5', '14', '121']
if all([int(i) > 0 for i in arr]) and any([j == j[::-1] for j in arr]):
    print(True)
else:
    print(False)
