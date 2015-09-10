""" Lecture 3 NEWTON-RAPHSON ROOT FINDING """

DX = 0.00001
PRECISION = 0.001

def close_enough(last, curr):
    return abs(last - curr) < PRECISION

def derivate(f):
    return lambda x: (f(x + DX) - f(x)) / DX
    
def next(f, x):
    return x - f(x) / derivate(f)(x)
    
def iteration(f, guess, last):
    print guess
    if close_enough(guess, last):
        return guess
    else:
        return iteration(f, next(f, guess), guess)
    
if __name__ == '__main__':
    f = lambda x: x ** 2 - 12345
    print(iteration(f, 12, 0))