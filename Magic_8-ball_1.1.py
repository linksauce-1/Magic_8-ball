# necessary modules and manual seed (just in case)
import random
import time
random.seed(time.process_time())
# response list
welcome = 'Welcome to the Magic 8-ball.\n'
thanks = '  Thank you for playing!\n'
details = '  Created by @linksauce_1. Copyright 2023.\n'
r1 = '  Keep your head up!\n'
r2 = '  You will die from a thing in a place.\n'
r3 = '  Computer over.\n  Virus = Very Yes.\n'
r4 = '  ChatGPT is requesting your current location.\n'
r5 = '  Time to check your car\'s oil level.\n'
r6 = '  Your life will improve. Eventually.\n'
r7 = '  Hypercritical is the best podcast ever made.\n  Don\'t @ me.\n'
r8 = '  Error 404: Wisdom not found.\n'
r9 = '  9 + 10 = 21.\n'
# main
print()
print(welcome)
while True:
    kpno = random.randint(1, 9)
    if kpno == 1:
        print(r1)
    elif kpno == 2:
        print(r2)
    elif kpno == 3:
        print(r3)
    elif kpno == 4:
        print(r4)
    elif kpno == 5:
        print(r5)
    elif kpno == 6:
        print(r6)
    elif kpno == 7:
        print(r7)
    elif kpno == 8:
        print(r8)
    else:
        print(r9)
    keepstate = input('Would you like to reshake the ball?\nEnter \'y\' to shake or \'n\' to exit: ')
    print()
    if keepstate == 'y':
        continue
    elif keepstate == 'n':
        print (thanks)
        break
print(details)