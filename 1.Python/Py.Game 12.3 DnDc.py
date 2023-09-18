import random

class Queen:
    def __init__(self, name, queen_type):
        self.name = name
        self.queen_type = queen_type
        self.health = 50
    
    def attack(self, target):
        damage = random.randint(1, 10)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
    
    def defend(self):
        print(f"{self.name} defends!")
    
    def heal(self):
        heal_amount = random.randint(2, 8)
        self.health = min(50, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount} health points.")

    def take_damage(self, damage):
        self.health -= damage

def play_game():
    queens = [
        Queen("Queen 1", "Oracle"),
        Queen("Queen 2", "Warrior"),
        Queen("Queen 3", "Druid"),
        Queen("Queen 4", "Elemental"),
        Queen("Queen 5", "Poisoner")
    ]
    
    current_turn = 0
    while True:
        current_queen = queens[current_turn]
        print(f"\n--- {current_queen.name}'s turn ---")
        
        # Roll the d20 dice
        dice_roll = random.randint(1, 20)
        print(f"Dice roll: {dice_roll}")
        
        if dice_roll in [1, 6, 11, 16]:
            action = current_queen.heal
        elif dice_roll in [2, 7, 12, 17]:
            action = current_queen.attack
        elif dice_roll in [3, 8, 13, 18]:
            action = current_queen.defend
        else:
            action = current_queen.attack
        
        # Perform the chosen action
        action(queens[random.randint(0, 4)])  # Choose a random target queen
        
        # Check if the game is over
        remaining_queens = [queen for queen in queens if queen.health > 0]
        if len(remaining_queens) == 1:
            print(f"\n{remaining_queens[0].name} wins the game!")
            break
        
        current_turn = (current_turn + 1) % 5
    
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()

# Start the game
play_game()
