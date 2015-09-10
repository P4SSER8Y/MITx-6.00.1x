""" Problem Set 1.1"""

s = 'azcbobobegghakl'

cnt = 0
for c in s:
    if c in 'aeiou':
        cnt = cnt + 1
print "Number of vowels:",cnt

""" Solution 2 """

print "Number of vowels:", s.count('a') + s.count('e') + s.count('i') \
      + s.count('o') + s.count('u')