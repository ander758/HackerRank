import re

"""
https://www.hackerrank.com/challenges/incorrect-regex/problem
github.com/ander758/HackerRank

You are given a string s.
Your task is to find out whether s is a valid regex or not.
"""


def is_regex_valid(str_regex):
    try:
        re.compile(str_regex)
        return True
    except re.error as e:
        return False


input_list = ['2', '.*\\+', '.*+']

for regex in input_list[1:]:
    print(is_regex_valid(str_regex=regex))
