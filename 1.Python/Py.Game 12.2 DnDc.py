import random

def start_game():
    print("Welcome to the Three Dark Crowns Game!")
    print("You are one of the triplet queens. Your goal is to defeat your sisters and claim the crown.")

    # add a d20 dice roll to chose each queen 
    # 1,6,11,16 is oracle. 
    # 2,7,12,17 is warrior. 
    # 3,8,13,18 is druid. 
    # 4,9,14,19 is elemental. 
    # 5,10,15,20 is poisoner
    dice_roll = random.randint(1, 20)
    if dice_roll in [1, 6, 11, 16]:
        current_queen = "Oracle"
    elif dice_roll in [2, 7, 12, 17]:
        current_queen = "Warrior"
    elif dice_roll in [3, 8, 13, 18]:
        current_queen = "Druid"
    elif dice_roll in [4, 9, 14, 19]:
        current_queen = "Elemental"
    else:
        current_queen = "Poisoner"

    print("You are a(n)", current_queen, "and possess", get_magical_ability(current_queen))

    print("Let the battle for the crown begin!")

    while True:
        action = input("What do you want to do? Attack [A], Defend [D], or Surrender [S]: ").upper()

        if action == "A":
            attacked_queen = random.choice(["Oracle", "Warrior", "Druid", "Elemental", "Poisoner"])
            if attacked_queen == current_queen:
                print("You attack but fail!")

            elif defeated(current_queen, attacked_queen):
                print("Congratulations! You defeated", attacked_queen, "and claimed the crown!")
                break

            else:
                print("You attack", attacked_queen, "but are defeated!")

        elif action == "D":
            print("You defend against any attacks.")

        elif action == "S":
            print("You surrender and your journey ends here.")
            break

        else:
            print("Invalid action. Please choose again.")

    print("\n************")
    play_again = input("Do you want to play again? [Y/N]: ")
    if play_again.upper() == "Y":
        start_game()
    else:
        print("Thank you for playing. Goodbye!")


def get_magical_ability(queen):
    # Return the magical ability of the queen
    return ""


def defeated(attacker, defender):
    # Determine if the attacker defeats the defender based on their magical abilities
    return random.choice([True, False])

start_game()