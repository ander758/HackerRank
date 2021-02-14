from random import randrange

"""
www.hackerrank.com/challenges/python-string-formatting/
github.com/ander758/HackerRank
"""


def print_formatted(number):
    for i in range(1, number + 1):
        w = len("{0:b}".format(n))
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))


if __name__ == '__main__':
    n = randrange(1, 99, 1)
    print_formatted(n)

# def strip_digits(string, removeFirstIfZero=False):
#    str_out = ''
#    for char in string:
#        if char.isdigit():
#            str_out += char
#    if removeFirstIfZero:
#        if str_out[0] == '0':
#            return str_out[1:]
#    return str_out


"""
Decimal | Octal | Hexadecimal | Binary
Sample input: 17
Sample output:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001  
"""
