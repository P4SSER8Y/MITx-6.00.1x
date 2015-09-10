def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    mid = len(aStr) / 2
    if aStr[mid] == char:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid + 1 :])
        
    
if __name__ == "__main__":
    assert isIn('a', 'abcdefghijklmn') == True
    assert isIn('o', 'abcdefghijklmn') == False
    assert isIn('k', 'abcdefghijklmn') == True
    assert isIn('n', 'abcdefghijklmn') == True