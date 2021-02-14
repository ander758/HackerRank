"""
www.hackerrank.com/challenges/text-wrap/
github.com/ander758/HackerRank

sample input: 4 ABCDEFGHIJKLIMNOQRSTUVWXYZ
output:
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""


def wrap(string, max_width):
    str_out, n = '', 0
    for char in string:
        str_out += char
        n += 1
        if n >= max_width:
            n = 0
            str_out += '\n'
    return str_out


if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4
    result = wrap(string, max_width)
    print(result)
