""" Practical Problem 1- Regular Ploygons 'funsum' """

""" https://docs.google.com/forms/d/1Lea6ZJlEVWsXcPiqPZ0JmGDDdvGO1OnXHAqNEtLu1cM/viewform?c=0&w=1 """
import math

def funsum(n, s):
    perimeter = n * s
    area = n * s * s / (4.0 * math.tan(math.pi / n))
    return round(area + perimeter * perimeter, 4)
    
if __name__ == "__main__":
    print funsum(7, 3)