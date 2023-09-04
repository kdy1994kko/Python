import pygame
from pygame.locals import *
import random
pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wassgoodiiee NEW GAME NAME HERE")

#define font
font = pygame.font.SysFont(None, 40)

# define game variables
score = 0

# define colors
bg = (255,200, 150)
body_inner =  (50,175, 25)
body_outer = (100,100, 200)
food_col = (200,50, 50)
blue = (0,0,255)
red = (255,0,0)

def draw_screen():
    screen.fill(bg)

def draw_score():
    score_txt = 'Score: ' + str(score)
    score_img = font.render(score_txt, True, blue)
    screen.blit(score_img, (0,0))

run = True
while run:
    draw_screen()

    draw_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()




pygame.quit()

