import pygame
import os

# initialization
pygame.init()

# set screen size
screen_width = 480
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set screen title
pygame.display.set_caption("rabbit survival")

# set background
current_dir = os.path.dirname(os.path.realpath(__file__))
background_file = current_dir + "/resource/googlelogo_color_272x92dp.png"
background = pygame.image.load(background_file)

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # set background by color
    screen.fill((0, 0, 255))
    # set background by image file
    screen.blit(background, (0, 0))
    # update game screen
    pygame.display.update()

# pygame shutdown
pygame.quit()