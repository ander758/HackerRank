
from random import randrange

"""
www.hackerrank.com/challenges/staircase
github.com/ander758/HackerRank

Sample Input
6 
Sample Output
     #
    ##
   ###
  ####
 #####
######
hackerrank.com/challenges/staircase/
"""

def replaceCharAtIndex(string, character, index):
    return string[:index] + character + string[index + 1:]

# Complete the staircase function below.
def staircase(n):
    output = ' ' * n
    for i in range(len(output), 0, -1):
        output = replaceCharAtIndex(output, '#', i - 1)
        print(f'{output}')


if __name__ == '__main__':
    n = randrange(1, 99, 1)
    staircase(n)

