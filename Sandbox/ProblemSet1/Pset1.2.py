"""Practice Again - Problem 2: Counting 'bob's"""

if __name__ == "__main__":
    s = 'azcbobobegghakl'

FIND = 'bob'
count = 0
for k in range(0, len(s)-len(FIND)+1):
    if s[k:k+len(FIND)] == FIND:
        count += 1
print "Number of times bob occurs is: " + str(count)
