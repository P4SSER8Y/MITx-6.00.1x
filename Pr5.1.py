def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    ret = 1
    while exp > 0:
        ret *= base
        exp -= 1
    return ret

if __name__ == "__main__":
        assert (2 ** 12) == iterPower(2, 12)