__author__ = 'troy'

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    answer = []
    valueList = aDict.values()
    for key in aDict.keys():
        if valueList.count(aDict[key]) == 1:
            answer.append(key)
    answer.sort()
    return answer

if __name__ == '__main__':
    print uniqueValues({})
    print uniqueValues({1: 1, 2: 2, 3: 1})
    print uniqueValues({1: 1, 2: 2, 3: 3})
    print uniqueValues({1: 1, 2: 1})
    print uniqueValues({3: 3, 2: 2, 1: 1})
    print uniqueValues({2: 0, 3: 3, 6: 1})