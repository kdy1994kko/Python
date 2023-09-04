import pygame
import random
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("D20 Dice Roller")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the dice class
class Dice(pygame.sprite.Sprite):
    def __init__(self):
        super(Dice, self).__init__()
        self.size = 100
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.value = 1

    def roll_dice(self):
        self.value = random.randint(1, 20)

    def draw(self, surface):
        # Draw hexagon
        radius = self.size // 2
        center_x, center_y = self.rect.center
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.radians(angle_deg)
            point_x = center_x + int(math.cos(angle_rad) * radius)
            point_y = center_y + int(math.sin(angle_rad) * radius)
            points.append((point_x, point_y))
        pygame.draw.polygon(surface, BLACK, points)

        # Draw value text
        font = pygame.font.Font(None, 100)
        text = font.render(str(self.value), True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

# Create dice object
dice = Dice()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            dice.roll_dice()

    # Update
    window.fill(WHITE)

    # Draw
    dice.draw(window)

    pygame.display.flip()

# Quit the game
pygame.quit()



# Save this code in a Python file, run it, and a Pygame window will open. 
# Click anywhere in the window to roll the d20 dice and see the result displayed in the center of the dice. 
# The window will close when you click the close button or close it through the window manager.