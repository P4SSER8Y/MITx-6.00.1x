def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])


if __name__ == "__main__":
    test = "Hello World!"
    assert len(test) == lenRecur(test)