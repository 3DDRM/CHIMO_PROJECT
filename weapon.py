import pygame

class Weapon():
    def __init__(self, image, width, height):
        self.image = image
        self.angle = 0
        self.width = width
        self.height = height
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.shape = self.image.get_rect()

    def update(self, player):
        self.shape.center = player.shape.center
        self.shape.x = self.shape.x + player.shape.width
        
    def draw(self, interface):
        interface.blit(self.image, self.shape)