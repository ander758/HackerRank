"""
https://www.hackerrank.com/challenges/symmetric-difference/problem
github.com/ander758/HackerRank

Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

input_01 = '2 4 5 9'
input_02 = '2 4 11 12'

ls = []
set_a = set(map(int, input_01.split(' ')))
set_b = set(map(int, input_02.split(' ')))

ls.append(set_a.difference(set_b))  # Remove same instances
ls.append(set_b.difference(set_a))  # Remove same instances

arr = []
for i in ls:
    for j in list(i):
        arr.append(j)
arr.sort()
[print(i) for i in arr]
