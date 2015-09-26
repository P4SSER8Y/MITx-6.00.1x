__author__ = 'troy'

def primesList(N):
    '''
    N: an integer
    '''
    # Your code here
    if N < 2:
        return []
    ans = [2]
    for i in range(3, N + 1, 2):
        isPrime = True
        for k in [x for x in ans if x <= int(i ** 0.5 + 1)]:
            if (i % k) == 0:
                isPrime = False
                break
        if isPrime:
            ans.append(i)
    return ans

if __name__ == "__main__":
    print primesList(1)
    print primesList(2)
    print primesList(3)
    print primesList(100)