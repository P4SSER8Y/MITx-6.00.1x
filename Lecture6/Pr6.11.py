def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxLen = -1
    maxKey = None
    for t in aDict.keys():
        if len(aDict[t]) > maxLen:
            maxLen = len(aDict[t])
            maxKey = t
    return maxKey

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print biggest(animals)