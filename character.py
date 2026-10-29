import pygame

class Character():
    def __init__ (self, x, y, image, width, height):
        self.image = image
        self.shape = self.image.get_rect()
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (width, height))
        self.shape.center = (x, y)

    def movement(self, delta_x, delta_y):
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y

    def draw(self, interface):
        interface.blit(self.image, self.shape)
        #pygame.draw.rect(interface, (255, 255, 0), self.shape)