import random

user_wins =0
computer_wins =0


options = ["rock", "paper", "scissors", "r", "p", "s"]

while True:
    user_input = input("Wassgoodiiee Type Rock (R) / Paper (P) / Scissors (S) or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,5)
    # rock = 0, paper = 1, scissors = 2, r = 3, p = 4, s = 5
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors" or user_input == "r" and computer_pick == "s":
        print("You \(^o^)/ Win")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock" or user_input == "p" and computer_pick == "r":
        print("You \(^o^)/ Win")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper" or user_input == "s" and computer_pick == "p":
        print("You \(^o^)/ Win")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "scissors" or user_input == "s" and computer_pick == "s":
        print("Double KYO. . Draw Go Again")
        user_wins += 0
    elif user_input == "rock" and computer_pick == "rock" or user_input == "r" and computer_pick == "r":
        print("Both Power Levels Are Over 9000. . Draw Go Again")
        user_wins += 0
    elif user_input == "paper" and computer_pick == "paper" or user_input == "p" and computer_pick == "p":
        print("Evenly Matched. . Draw Go Again")
        user_wins += 0
    elif user_input == "r" and computer_pick == "scissors" or user_input == "rock" and computer_pick == "s":
        print("You \(^o^)/ Win")
        user_wins += 1
    elif user_input == "p" and computer_pick == "rock" or user_input == "paper" and computer_pick == "r":
        print("You \(^o^)/ Win")
        user_wins += 1
    elif user_input == "s" and computer_pick == "paper" or user_input == "scissors" and computer_pick == "p":
        print("You \(^o^)/ Win")
        user_wins += 1
    elif user_input == "s" and computer_pick == "scissors" or user_input == "scissors" and computer_pick == "s":
        print("Double KYO. . Draw Go Again")
        user_wins += 0
    elif user_input == "r" and computer_pick == "rock" or user_input == "rock" and computer_pick == "r":
        print("Both Power Levels Are Over 9000. . Draw Go Again")
        user_wins += 0
    elif user_input == "p" and computer_pick == "paper" or user_input == "paper" and computer_pick == "p":
        print("Evenly Matched. . Draw Go Again")
        user_wins += 0
    else:
        print(" El Oh EL Woowww, Thats Crazy. . You Lost Again")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("GG's Peace Out")
