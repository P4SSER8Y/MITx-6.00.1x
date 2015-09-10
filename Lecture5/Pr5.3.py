def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    def odd(n):
        return (n % 2) == 1
    if exp == 0:
        return 1
    elif odd(exp):
        return base * recurPowerNew(base, exp - 1)
    else:
        return recurPowerNew(base * base, exp / 2)


if __name__ == "__main__":
    assert 2 ** 30 == recurPowerNew(2, 30)