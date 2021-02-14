"""
www.hackerrank.com/challenges/string-validators
github.com/ander758/HackerRank

Check if string contains:
alphanumeric characters,
alphabetical characters,
digits,
lowercase,
uppercase characters.
"""


def validate_string(s):
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))
    # validity_dict = {
    #    'alphanumeric': False,
    #    'alphabetical': False,
    #    'digits': False,
    #    'lowercase': False,
    #    'uppercase': False
    # }
    # for char in s:
    #    if char.isalnum():
    #        validity_dict['alphanumeric'] = True
    #    if char.isalpha():
    #        validity_dict['alphabetical'] = True
    #    if char.isdigit():
    #        validity_dict['digits'] = True
    #    if char.islower():
    #        validity_dict['lowercase'] = True
    #    if char.isupper():
    #        validity_dict['uppercase'] = True
    # for key in validity_dict:
    #    print(f'{key}={validity_dict.get(key)}')


if __name__ == '__main__':
    s = 'qA2'
    validate_string(s)
