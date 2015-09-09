def printMove(fr, to):
    print "move from " + str(fr) + " to " + str(to)
    
def Hanoi(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Hanoi(n - 1, fr, spare, to)
        Hanoi(1, fr, to , spare)
        Hanoi(n - 1, spare, to, fr)
        
if __name__ == "__main__":
    print "One plate"
    Hanoi(1, 'A', 'C', 'B')
    print
    print "Two plates"
    Hanoi(2, 'A', 'C', 'B')
    print
    print "Three plates"
    Hanoi(3, 'A', 'C', 'B')