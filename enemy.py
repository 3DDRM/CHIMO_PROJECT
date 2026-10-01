import pygame
import time
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, health):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.moving = True
        self.timer = 0
        self.tick = 60

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 100, 0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, walls):
        x_old = self.rect.x
        self.timer += 1

        if self.moving:
            if self.timer >= self.tick:
                self.rect.x += self.speed
                self.timer = 0
                self.moving = False

        if not self.moving:
            if self.timer >= self.tick:
                self.rect.y += self.speed
                self.timer = 0
                self.moving = True


    def draw(self, surface):
        surface.blit(self.image, self.rect)




