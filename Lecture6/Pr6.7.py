def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]
print testList

list7A = testList[:]
applyToEach(list7A, abs)
print list7A

list7B = testList[:]
applyToEach(list7B, lambda (x): x + 1)
print list7B

list7C = testList[:]
applyToEach(list7C, lambda (x): x ** 2)
print list7C