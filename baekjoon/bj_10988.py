import sys


word = list(str(input()))

# print(word[::-1])

if list(reversed(word)) == word:
    print('1')
else:
    print('0')

# print('1' if word == word[::-1] else '0')
