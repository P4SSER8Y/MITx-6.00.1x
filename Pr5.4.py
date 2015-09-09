def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while b != 0:
        t = a % b
        a = b
        b = t
    return a
    
if __name__ == "__main__":
    assert gcdIter(2, 12) == 2
    assert gcdIter(6, 12) == 6
    assert gcdIter(12, 6) == 6
    assert gcdIter(9, 12) == 3
    assert gcdIter(7, 12) == 1