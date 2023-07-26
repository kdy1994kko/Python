print('Wassgoodiiee Welcome To YOUR OWN ADVENTURE \(^0^)/')
name = input("What is your name ?? ")
playing= input("Wassgoodiiee " + name + " Wanna Play A Game ?? Yes Or No. .")
if playing.lower() != 'yes':
    print('Then Bye Bitch, Nobody Wanted Yo Stank Ass To Play ANYYY WAYYY')
    quit()
print("Okay Let's Play \(^0^)/")
level = 0
answer= input("Its dark and something is chasing you on your way home && theres a fork in the dirt road. THINK FAST, Do you want to go left or right?? ").lower()
if answer =='left':
    answer = input("You come to a river, do you swim through or walk around?? (Walk/Swim) ").lower()

    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")
    elif answer == "walk":
        print("Yooo that's crazy. . you walked for many miles, ran out of water && you lost the game")
    else:
        print("el oh el not a valid option. .TOO SLOW YOU LOSE")

elif answer =='right':
    answer= input("You come to a bridge, it looks wobbly, do you want to cross it or head back?? (Cross/Back) ").lower()

    if answer == "back":
        print("Wrong choice, you got caught by your stalker and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them ?? (Yes/No) " )

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended && shoots you with their gun and you lose.")

    else:
        print("el oh el not a valid option. .TOO SLOW YOU LOSE")

else:
    print("el oh el not a valid option. .TOO SLOW YOU LOSE")

print("Try Again ??")
