"""Practice Again - Problem 3: Alphabetical Substrings"""

def foo(s):
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

if __name__ == "__main__":
    s = 'azcbobobegghakl'
    foo(s)