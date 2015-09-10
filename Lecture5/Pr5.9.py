def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    if (str1 == '') and (str2 == ''):
        return True
    elif (str1 == '') or (str2 == ''):
        return False
    elif (str1[0] != str2[-1]):
        return False
    else:
        return semordnilap(str1[1:], str2[:-1])
    
# === Something Additional ===
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
if __name__ == "__main__":
    assert semordnilapWrapper('abc', 'cba') == True
    assert semordnilapWrapper('aaaaa', 'aaaaa') == False
    assert semordnilapWrapper('abc', 'cbas') == False
    assert semordnilapWrapper('abc', 'cca') == False