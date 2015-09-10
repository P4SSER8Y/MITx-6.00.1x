#L5.Recursion on Strings -- Palindromes

def isPalindromes(s):
    def removeUselessChar(s):
        s = s.lower()
        t = ''
        for c in s:
            if ('a' <= c) and (c <= 'z'):
                t = t + c
        return t
    def recurPar(s):
        if len(s) <= 1:
            return True
        elif s[0] == s[-1]:
            return recurPar(s[1:-1])
        else:
            return False
    return recurPar(removeUselessChar(s))