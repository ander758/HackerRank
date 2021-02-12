import string

# TODO: Fix testcase 0, 4 and 4

"""
www.hackerrank.com/challenges/alphabet-rangoli/
"""


def print_rangoli(size):
    arr = []
    for i in range(size - 1, 0, -1):
        indices = ''
        for k in range(size - i):
            indices += str(k)
        arr.append(indices + (indices[::-1])[1:])

    for i in range(0, size):
        indices = ''
        for k in range(0, size - i):
            indices += str(k)
        arr.append(indices + (indices[::-1])[1:])

    for indices in arr:
        line = ''
        chars = [char for char in string.ascii_lowercase][:size][::-1]  # Reversed n-long alphabet
        for char in indices:
            line += chars[int(char)] + '-'
        print(line[:-1].center(size * 4 - 3, '-'))  # Print out with max width and '-'padding


if __name__ == '__main__':
    size = 10
    print_rangoli(size)

"""
size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
"""
