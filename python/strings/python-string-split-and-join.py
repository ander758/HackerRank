"""
www.hackerrank.com/challenges/python-string-split-and-join/
github.com/ander758/HackerRank
"""


def split_and_join(line):
    return line.replace(' ', '-')


if __name__ == '__main__':
    line = 'this is a string'
    result = split_and_join(line)
    print(result)
