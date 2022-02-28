import pygame

# initialization
pygame.init()

# set screen size
screen_width = 480
screen_height = 600
pygame.display.set_mode((screen_width, screen_height))

# set screen title
pygame.display.set_caption("rabbit survival")

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame shutdown
pygame.quit()