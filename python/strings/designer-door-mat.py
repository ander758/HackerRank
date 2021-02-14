"""
www.hackerrank.com/challenges/designer-door-mat/
github.com/ander758/HackerRank
"""


def get_doormat(w, h, padding_outer, padding_inner, text):
    str_out = ''
    for i in range(1, h, 2):
        str_out += (i * padding_inner).center(w, padding_outer) + '\n'
    str_out += text.center(w, padding_outer) + '\n'
    for i in range(h - 2, -1, -2):
        str_out += (i * padding_inner).center(w, padding_outer) + '\n'
    return str_out


print(get_doormat(w=33, h=11, padding_inner='.|.', padding_outer='-', text='WELCOME'))

"""
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
"""
