"""
www.hackerrank.com/challenges/find-a-string
github.com/ander758/HackerRank

Count occurrences of substrings in a string
"""


def count_substring(string, sub_string):
    n, cache = 0, ''
    for char in string:
        cache += char
        if cache[-len(sub_string):] == sub_string:
            n += 1
    return n


if __name__ == '__main__':
    string, sub_string = 'Hello my name is Anders. Anders is cool >:)', 'Anders'
    count = count_substring(string, sub_string)
    print(count)
