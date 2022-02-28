import pygame
import os
from pygame.constants import K_DOWN, K_UP
from entityClass import Entity

###################################################################################################
# 0. basic initialization
###################################################################################################
pygame.init()

# set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set screen title
pygame.display.set_caption("yuji vs ddong")

# set clock
clock = pygame.time.Clock()

# set current directory
current_dir = os.path.dirname(os.path.realpath(__file__))
resource_dir = current_dir + "/../resource"

gameOver = False
gameOverInterval = 3
gameOverTime = 0
###################################################################################################
# 1. user initialization (background, image, location, speed, font)
###################################################################################################

# set background
# none

# set game title
# none

# font info
# create font instance (font style, size)
game_font = pygame.font.Font(None, 40)

# set background music
bgmFile = resource_dir + "/ddong_bgm.mp3"
pygame.mixer.music.load(bgmFile)
pygame.mixer.music.set_volume(0.3)

# ddong sound
ddongSoundFile = resource_dir + "/ddong_effect.wav"
ddongSoundEffect = pygame.mixer.Sound(ddongSoundFile)
ddongSoundEffect.set_volume(0.7)
# gameover sound
gameoverSoundFile = resource_dir + "/gameover_sound.mp3"
gameoverSoundEffect = pygame.mixer.Sound(gameoverSoundFile)
# gameoverSoundEffect.set_volume(0.7)

# destination
toX = 0

# time, ms
startTicks = pygame.time.get_ticks()
ssanTime = startTicks
ddongInterval = 3000
minInterval = 100

# load user image
userFile = resource_dir + "/yuji.png"
ddongFile = resource_dir + "/ddong.png"
gameOverFile = resource_dir + "/gameover2.png"
user = Entity("user", "yu-ji", userFile)

# create ddong list
ddongList = []
ddongNum = 0

def createDdong()->None:
    global ddongList
    global ddongNum
    ddongList.append(Entity("ddong", "ddong", ddongFile))
    ddongSoundEffect.play()


def moveAllDdong()->None:
    global ddongNum
    for entry in ddongList:
        entry.move(0, 1)
        if entry.rectangle.y > screen_height:
            ddongNum += 1
            ddongList.remove(entry)
            del(entry)

def calcBoundary():
    # set x boundary
    if user.rectangle.left < 0:
        user.rectangle.left = 0
    elif user.rectangle.left > screen_width - user.rectangle.width:
        user.rectangle.left = screen_width - user.rectangle.width
    # set y boundary
    if user.rectangle.top < 0:
        user.rectangle.top = 0
    elif user.rectangle.top > screen_height - user.rectangle.height:
        user.rectangle.top = screen_height - user.rectangle.height

def showGameOver():
    global gameOver
    global gameOverTime
    gameOver = True
    gameOverTime = pygame.time.get_ticks() / 1000
    Entity("gameover", "gameover", gameOverFile)


def checkGameEnd():
    global running
    if pygame.time.get_ticks() / 1000 - gameOverTime > gameOverInterval:
        running = False


###################################################################################################
# main event loop
###################################################################################################
running = True

# turn on background music
pygame.mixer.music.play(-1)

while running:
    # set FPS
    dt = clock.tick(60)

    # event loop (keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                toX -= 1
            if event.key == pygame.K_RIGHT:
                toX += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0

    if gameOver == False:
        ddongTimer = pygame.time.get_ticks() - ssanTime
        if ddongTimer >= ddongInterval:
            createDdong()
            ssanTime = pygame.time.get_ticks()
            if ddongInterval > minInterval:
                ddongInterval *= 0.9

        # set character location
        user.move(toX, 0)

        # check boundary
        calcBoundary()

        # move ddong
        moveAllDdong()

        # check collision
        for x in ddongList:
            if (user.rectangle.colliderect(x.rectangle)):
                print("collision, game over")
                gameoverSoundEffect.play()
                showGameOver()
                break

        # set background by color
        screen.fill((0, 0, 255))
        # set instances
        for x in Entity.entityList:
            screen.blit(x.image, (x.rectangle.x, x.rectangle.y))
    else:
        checkGameEnd()

    ddongScore = game_font.render(("Score : " + str(ddongNum)), True, (255, 255, 255))
    # set score
    screen.blit(ddongScore, (0, 0))
    # update game screen
    pygame.display.update()

# pygame shutdown
pygame.quit()