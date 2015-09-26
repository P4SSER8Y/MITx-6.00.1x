__author__ = 'troy'

# Part 1
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a * (x ** 2) + b * x + c

# Part 2
def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here
    print evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)

if __name__ == "__main__":
    pass