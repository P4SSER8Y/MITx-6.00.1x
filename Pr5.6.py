def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    n = 0
    while aStr != '':
        n += 1
        aStr = aStr[1:]
    return n    

if __name__ == "__main__":
    test = "Hello World!"
    assert len(test) == lenIter(test)