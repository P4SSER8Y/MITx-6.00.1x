__author__ = 'troy'



def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    k = 0
    while k < len(L):
        if f(L[k]):
            k = k + 1
        else:
            L.remove(L[k])
    return len(L)

#run_satisfiesF(L, satisfiesF)

if __name__ == "__main__":
    def f(s):
        return 'a' in s
    L = ['a']
    print satisfiesF(L)
    print L