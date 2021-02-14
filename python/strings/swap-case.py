"""
www.hackerrank.com/challenges/swap-case
github.com/ander758/HackerRank
"""


def swap_case(s):
    s_swapped = ''
    for char in s:
        if char.isupper():
            s_swapped += char.lower()
        else:
            s_swapped += char.upper()
    return s_swapped


if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)
