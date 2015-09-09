def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

if __name__ == "__main__":
    gcdIter = gcdRecur
    assert gcdIter(2, 12) == 2
    assert gcdIter(6, 12) == 6
    assert gcdIter(12, 6) == 6
    assert gcdIter(9, 12) == 3
    assert gcdIter(7, 12) == 1