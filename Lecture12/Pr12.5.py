def genPrimes():
    primes = [2]
    yield 2
    k = 3
    while True:
        flag = True
        for x in [y for y in primes if (y * y) <= k]:
            if (k % x == 0):
                flag = False
                break
        if flag:
            primes.append(k)
            yield k
        k += 2

if __name__ == "__main__":
    primes = genPrimes()
    for _ in range(100):
        print primes.next()
