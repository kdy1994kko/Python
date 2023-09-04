import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissors.png')

# Create player and computer choices
choices = ["rock", "paper", "scissors"]
player_choice = ""
computer_choice = ""

# Create game result
result = ""

def display_choices():
    x = WIDTH // 4
    y = HEIGHT // 3

    screen.blit(rock_img, (x - 150, y - 50))
    screen.blit(paper_img, (x - 50, y - 50))
    screen.blit(scissors_img, (x + 50, y - 50))

def display_result():
    font = pygame.font.SysFont(None, 64)
    text = font.render(result, True, WHITE)
    x = WIDTH // 2 - text.get_width() // 2
    y = HEIGHT // 2 - text.get_height() // 2
    screen.blit(text, (x, y))

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = WIDTH // 4
            y = HEIGHT // 3
            if (x - 150) < mouse_pos[0] < (x - 50) and (y - 50) < mouse_pos[1] < (y + 100):
                player_choice = "rock"
            elif (x - 50) < mouse_pos[0] < (x + 50) and (y - 50) < mouse_pos[1] < (y + 100):
                player_choice = "paper"
            elif (x + 50) < mouse_pos[0] < (x + 150) and (y - 50) < mouse_pos[1] < (y + 100):
                player_choice = "scissors"
            computer_choice = get_computer_choice()
            result = determine_winner(player_choice, computer_choice)

    display_choices()
    if player_choice and computer_choice:
        display_result()

    pygame.display.flip()

# Quit the game
pygame.quit()
