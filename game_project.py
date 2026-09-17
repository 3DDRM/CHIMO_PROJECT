import pygame
import constants
import objects
import time

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption('CHIMO ADVENTURE SUPREME')
window.fill((0,0,0))

music = pygame.mixer.music.load('assets//songs//More.mp3')
music = pygame.mixer.music.play(-1)


player = pygame.image.load('assets//images//characters//player//walk_0.png').convert_alpha()
background = pygame.image.load('assets//images//backgrounds//Stage_1.png').convert()

player = pygame.transform.scale(player, (100, 110))
background = pygame.transform.scale(background, (constants.STAGE_WIDTH, constants.STAGE_HEIGHT))

player_width = player.get_width()
player_height = player.get_height()

x = 350
y = 250

walls =[
    objects.Wall(35, 480, 210, 20),
    objects.Wall(730, 100, 30, 150),
    objects.Wall(70, 135, 20, 20),
    objects.Wall(750, 500, 30, 100)
]

loocking_right = True
clock = pygame.time.Clock()
game = True
while game:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pressed = pygame.key.get_pressed()

    x_old = x
    y_old = y

    if pressed[pygame.K_w]:
        y -= constants.SPEED
    if pressed[pygame.K_s]:
        y += constants.SPEED
    if pressed[pygame.K_d]:
        x += constants.SPEED
        if loocking_right:
            player = pygame.transform.flip(player, True, False)
            loocking_right = False
    if pressed[pygame.K_a]:
        x -= constants.SPEED
        if not loocking_right:
            player = pygame.transform.flip(player, True, False)
            loocking_right = True

    if x > (window.get_width() - player_width - 10):
        x = window.get_width() - player_width - 10

    if x < constants.EDGE:
        x = constants.EDGE

    if y > (window.get_height() - player_height - constants.EDGE):
        y = window.get_height() - player_height - constants.EDGE

    if y < 60:
        y = 60

    player_rect = pygame.Rect(x, y, player_width, player_height)

    for i in walls:
        if player_rect.colliderect(i.rect):
            x = x_old
            y = y_old
            break   

    window.fill((0,0,0))
    window.blit(background, (0, 0))               
    window.blit(player, (x,y))

    pygame.display.update()

pygame.quit()