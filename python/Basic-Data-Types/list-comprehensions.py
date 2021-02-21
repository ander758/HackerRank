"""
https://www.hackerrank.com/challenges/list-comprehensions/problem
github.com/ander758/HackerRank

Print all possible coordinates where sum(x,y,z) != n
"""

x = 1
y = 1
z = 1
n = 2

_xyz = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                _xyz.append([i, j, k])

_xyz = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n]

print(_xyz)
