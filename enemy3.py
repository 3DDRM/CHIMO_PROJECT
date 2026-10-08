import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, health):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.step = 1
        self.timer = 0
        self.tick = 60

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 100, 0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        x_old = self.rect.x
        self.timer += 1

        if self.step == 1:
            if self.timer >= self.tick:
                self.rect.x+= self.speed
                self.timer = 0
                self.step = 2
                
        if self.step == 2:
            if self.timer >= self.tick:
                self.rect.x-= self.speed
                self.timer = 0
                self.step = 1
                
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)


    def draw(self, surface):
        surface.blit(self.image, self.rect)