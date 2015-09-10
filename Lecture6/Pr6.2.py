def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[::2]
    
if __name__ == '__main__':
    assert oddTuples(('I', 'am', 'a', 'test', 'tuple')) == ('I', 'a', 'tuple')
