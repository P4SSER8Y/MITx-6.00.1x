"""Practice Again - Problem 1: Counting Vowels"""

cnt = 0
for c in s:
    if c in 'aeiou':
        cnt = cnt + 1
print "Number of vowels:",cnt