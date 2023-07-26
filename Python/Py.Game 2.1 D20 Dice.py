#sometimes you don't have a D20 lying around for Dungeons and Dragons...
#so let's code one

#first, import random capabilities
import random

#let's make a loop that allows us to use the die repetitively
while True:
    #this now asks the user to press enter to roll at the beginning
    input ("Press enter to roll a D20")
    #this sets a random integer from 1 to 20 to our d20 variable
    d20 = random.randint (1,20)
    print (d20)
    #now let's interpret the outcomes of the D20 for 20 and 1
    if d20 == 1:
        print ("CRITICAL FAIL..You Suck")
    elif d20 == 20:
        print ("CRITICAL HIT(^O^)IT'S OVER 9000")
