"""
www.hackerrank.com/challenges/ginorts/

You are given a string str_in
str_in contains alphanumeric characters only.
Your task is to sort the string  in the following manner:
    - All sorted lowercase letters are ahead of uppercase letters.
    - All sorted uppercase letters are ahead of digits.
    - All sorted odd digits are ahead of sorted even digits.
E.g. input: Sorting1234
output: ginortS1324
"""

str_in = 'Sorting1234'

# Split uppercase, lowercase, odd-/even-numerics in 4 lists and extract each type
arr_upper, arr_lower, arr_odd, arr_even = [], [], [], []
for char in str_in:
    try:
        if int(char) % 2 == 0:
            arr_even.append(char)
        else:
            arr_odd.append(char)
    except:
        if char.isupper():
            arr_upper.append(char)
        elif char.islower():
            arr_lower.append(char)

# Print each element in all 4 lists sorted
print(''.join(i for i in
              sorted(arr_lower) + sorted(arr_upper) +
              sorted(arr_odd) + sorted(arr_even)))
