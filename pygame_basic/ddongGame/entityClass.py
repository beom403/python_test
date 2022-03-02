# entity class for ddong game

import pygame
from dataclasses import dataclass, field
import random

from pygame import image

# constant
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Entity:
    # static variables
    entityList = []
    speed = 10
    defaultObjectSize = 50

    def __init__(self, type, name, imageDirectory, width = defaultObjectSize, height = defaultObjectSize) -> None:
        print("create ", name)
        # init attributes
        self.type = type
        self.name = name
        self.imageDirectory = imageDirectory
        self.image = pygame.image.load(imageDirectory)
        if type == "user" or type == "USER":
            # transform image scale
            self.image = pygame.transform.scale(self.image, (width, height))
            # get rectangle
            self.rectangle = self.image.get_rect()
            # set init location
            self.rectangle.x = WINDOW_WIDTH / 2 - self.rectangle.width / 2
            self.rectangle.y = WINDOW_HEIGHT - self.rectangle.height
        elif type == "gameover" or type == "GAMEOVER":
            # get rectangle
            self.rectangle = self.image.get_rect()
            self.rectangle.x = WINDOW_WIDTH / 2 - self.rectangle.width / 2
            self.rectangle.y = WINDOW_HEIGHT / 2 - self.rectangle.height / 2
        else:   # ddong
            # transform image scale
            self.image = pygame.transform.scale(self.image, (width, height))
            # get rectangle
            self.rectangle = self.image.get_rect()
            # set init location
            self.rectangle.x = random.randrange(0, WINDOW_WIDTH - self.rectangle.width)
            self.rectangle.y = 0
        # append to instance list
        Entity.entityList.append(self)
        # print rect info
        # print("name : ", self.name, ", rect : ", self.rectangle)

    def __del__(self) -> None:
        print("delete ", self.name)

    def move(self, x, y) -> None:
        self.rectangle.left += x * Entity.speed
        self.rectangle.top += y * Entity.speed

