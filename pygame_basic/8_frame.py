import pygame
import os

from pygame.constants import K_DOWN, K_UP

###################################################################################################
# 0. basic initialization
###################################################################################################
pygame.init()

# set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set screen title
pygame.display.set_caption("game title")

# set clock
clock = pygame.time.Clock()


###################################################################################################
# 1. user initialization (background, image, location, speed, font)
###################################################################################################


# event loop
running = True
while running:
    # set FPS
    dt = clock.tick(60)

    # 2. event loop (keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. set character location

    # 4. collision event
    
    # 5. update game screen
    pygame.display.update()

# pygame shutdown
pygame.quit()