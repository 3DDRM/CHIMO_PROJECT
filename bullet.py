import pygame 

class Bullet():
    def __init__(self, weapon, image, speed, width, height):
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.shape = self.image.get_rect()
        self.shape.center = weapon.shape.center
        self.speed = speed

    def update(self):
        self.shape.x += self.speed

    def draw(self, interface):
        interface.blit(self.image, self.shape)