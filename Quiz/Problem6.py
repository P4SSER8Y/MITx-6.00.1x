__author__ = 'troy'

def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N == 0:
        return 0
    elif (N % 10 == 7):
        return count7(N / 10) + 1
    else:
        return count7(N / 10)

if __name__ == "__main__":
    print 171, count7(171)
    print 1234567, count7(1234567)
    print 77777777, count7(77777777)
    print 0, count7(0)
    print 8989, count7(8988)