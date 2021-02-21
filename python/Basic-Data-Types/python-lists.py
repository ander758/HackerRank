"""
https://www.hackerrank.com/challenges/python-lists/problem
github.com/ander758/HackerRank


"""

arr = []
inputs = ['12', 'insert 0 5', 'insert 1 10', 'insert 0 6',
          'print', 'remove 6', 'append 9', 'append 1',
          'sort', 'print', 'pop', 'reverse', 'print']

for _input in inputs[1:]:
    _input = _input.split(' ')
    method = _input[0].lower()
    args = [int(arg) for arg in _input[1:]]

    if method == 'insert':
        arr.insert(args[0], args[1])
    elif method == 'print':
        print(arr)
    elif method == 'remove':
        arr.remove(args[0])
    elif method == 'append':
        arr.append(args[0])
    elif method == 'sort':
        arr.sort()
    elif method == 'pop':
        arr.pop()
    elif method == 'reverse':
        arr.reverse()
