"""
www.hackerrank.com/challenges/python-mutations
"""

def mutate_string(string, position, character):
    arr = list(string)
    arr[position] = character
    return ''.join(arr)

if __name__ == '__main__':
    s = 'abracadabra'
    i = '5'
    c = 'k'
    s_new = mutate_string(s, int(i), c)
    print(s_new)