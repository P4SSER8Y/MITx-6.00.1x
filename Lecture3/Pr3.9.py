""" L3 PROBLEM 9 """

print "Please think of a number between 0 and 100!"

s , e = 0, 100
while True:
    mid = (s + e) / 2
    print "Is your secret number", mid, "?"
    print "Enter 'h' to indicate the guess is too high.", 
    print "Enter 'l' to indicate the guess is too low.",
    print "Enter 'c' to indicate I guessed correctly.",
    cmd = raw_input()
    if cmd == 'h':
        e = mid
    elif cmd == 'l':
        s = mid
    elif cmd == 'c':
        break;
    else:
        print "Sorry, I did not understand your input."
        
print "Game over. Your secret number was:", mid