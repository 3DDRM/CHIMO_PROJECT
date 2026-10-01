import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))

    def draw(self, surface):
        surface.blit(self.image, self.rect)