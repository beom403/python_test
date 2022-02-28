import pygame
import os

from pygame.constants import K_DOWN, K_UP

# initialization
pygame.init()

# set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set screen title
pygame.display.set_caption("tokki survival")

# set background
current_dir = os.path.dirname(os.path.realpath(__file__))
background_file = current_dir + "/resource/googlelogo_color_272x92dp.png"
background = pygame.image.load(background_file)

# set game title
main_title_file = current_dir + "/resource/main_title.png"
main_title = pygame.image.load(main_title_file)

# set clock
clock = pygame.time.Clock()

# transform scale
main_title = pygame.transform.scale(main_title, (300, 200))

main_title_size = main_title.get_rect().size
main_title_width = main_title_size[0]
main_title_height = main_title_size[1]
main_title_x_pos = screen_width / 2 - main_title_width / 2
main_title_y_pos = 0

# load character
character_file = current_dir + "/resource/Chic.png"
character = pygame.image.load(character_file)
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# transform scale
character = pygame.transform.scale(character, (character_width / 2, character_height / 2))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height / 2 - character_height / 2

# destination
to_x = 0
to_y = 0

# speed of character
character_speed = 0.5

# event loop
running = True
while running:
    # set FPS
    dt = clock.tick(60)
    # print FPS
    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # move character
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # set x boundary
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # set y boundary
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # set background by color
    screen.fill((0, 0, 255))
    # set background by image file
    screen.blit(main_title, (main_title_x_pos, main_title_y_pos))
    # set character
    screen.blit(character, (character_x_pos, character_y_pos))
    # update game screen
    pygame.display.update()

# pygame shutdown
pygame.quit()