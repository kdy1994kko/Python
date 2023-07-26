print('Wassgoodiiee Welcome To My KYO Quiz \(^0^)/')

name = input("What is your name ?? ")

playing= input("Wassgoodiiee " + name + " Wanna Play A Game ?? Yes Or No. .")

if playing.lower() != 'yes':
    print('Then Bye Bitch, Nobody Wanted Yo Stank Ass To Play ANYYY WAYYY')
    quit()

print("Okay Let's Play \(^0^)/")
score = 0

answer= input("What Is Kevvan's Favorite Color?? Hint It's 3 Letters ")
if answer.lower() =='red':
    print('AYYEEEE LEETTTSSS GOOOO')
    score +=1
else:
    print("Wow That's Crazy, Try Again")

answer = input("What Is Kevvan's Favorite Food?? Hint It's 5 Letters ")
if answer.lower() == 'bacon':
    #elif answer.lower == 'zebra cakes':
    #elif answer.lower =='food':
    #elif answer.lower == 'anything':
    print('AYYEEEE LEETTTSSS GOOOO')
    score += 1
else:
    print("Really. . No Nigga, Try Again")

answer = input("What Is Kevvan's Favorite Word?? Hint It's 4 Letters ")
if answer.lower() == 'both':
    print('AYYEEEE LEETTTSSS GOOOO')
    score += 1
else:
    print("I Don't Think You Know Me, Try Again")

answer = input("What Is Kevvan's Favorite FPS BR Game?? Hint It's 4 Letters ")
if answer.lower() == 'apex':
   # elif =='apex legends':
    print('AYYEEEE LEETTTSSS GOOOO')
    score += 1
else:
    print("Whhhaatt How Do You Not Know This, Try Again")

print("You Got " + str(score) + " Of 4 Questions Correct WOO WOO WOO")
print("Your Score Is " + str((score/4) * 100) + "%.")
