"""Practice Again - Problem 3: Alphabetical Substrings"""

def foo1(s):
    k = 0
    longestString = ''
    while k < len(s):
        currString = s[k]
        while (k + 1 < len(s)) and (s[k] <= s[k+1]):
            k += 1
            currString += s[k]
        if len(currString) > len(longestString):
            longestString = currString
        k += 1
    print "Longest substring in alphabetical order is: " + longestString

def foo2(s):
    def iter(curr, left):
        if len(left)>0:
            if (len(curr) == 0) or (curr[-1] <= left[0]):
                return iter(curr + left[0], left[1:])
            else:
                if len(curr) >= len(iter('', left)):
                    return curr
                else:
                    return iter('', left)
        else:
            return curr
    print "Longest substring in alphabetical order is: " + iter('', s)

def foo3(s):
    def check(s):
        for k in range(0, len(s) - 1):
            if s[k] > s[k + 1]:
                return False
        return True
    for length in range(len(s), 0, -1):
        for k in range(0, len(s) - length + 1):
            if check(s[k:k + length]):
               print "Longest substring in alphabetical order is: " + s[k:k + length]
               return None

if __name__ == "__main__":
    s = 'azcbobobegghakl'
    foo1(s)
    foo2(s)
    foo3(s)