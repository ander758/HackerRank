import os


arr = [i for i in os.walk('../python')]
print(arr[0][1])

print([i for i in os.walk('../python')][0][1])

subject_dict = {
    'python': ['py'] + ([i for i in os.walk('../python')][0][1])
}
for key in subject_dict:
    print(subject_dict.get(key))
