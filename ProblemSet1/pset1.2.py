""" sandbox 1.2 """

s = 'bobobobobobobobob'

cmp_str = 'bob'
cnt = 0

for k in range(len(s)-len(cmp_str)+1):
    if s[k:k+len(cmp_str)] == cmp_str:
        cnt += 1
print 'Number of times bob occurs is:',cnt