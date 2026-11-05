import pygame
import constants
import objects
import enemy
import enemy2
import enemy3
import character
import weapon
import bullet

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption('CHIMO ADVENTURE SUPREME')
window.fill((0,0,0))

music = pygame.mixer.music.load('assets//songs//practice_mode.mp3')
music = pygame.mixer.music.play(-1)

x = 500
y = 300

player_image = pygame.image.load('assets//images//characters//player//shovel_knight.png').convert_alpha()
background = pygame.image.load('assets//images//backgrounds//Stage_1.png').convert()

player_image = pygame.transform.scale(player_image, (70, 70))
background = pygame.transform.scale(background, (constants.STAGE_WIDTH, constants.STAGE_HEIGHT))

player = character.Character(x, y, player_image,  100, 80)

#player_width = player.shape.width
#player_height = player.shape.height

walls =[
    objects.Wall(40, 440, 210, 90),
    objects.Wall(700, 120, 50, 150),
    objects.Wall(50, 135, 40, 40),
    objects.Wall(705, 450, 80, 110)
]

ammu = []

enemy_image = pygame.image.load('assets//images//characters//enemy//rat_sprite.png').convert_alpha()
enemy_image_two = pygame.image.load('assets//images//characters//enemy//rat_invert.png').convert_alpha()
gun_image = pygame.image.load('assets//images//weapons//torchic.webp').convert_alpha()
shot_image = pygame.image.load('assets//images//weapons//bullet.png').convert_alpha()

enemie1 = enemy.Enemy(100, 200, enemy_image, 140, 70, 100, 2)
enemie2 = enemy2.Enemy(400, 400, enemy_image, 140, 70, 100, 2)
enemie3 = enemy3.Enemy(480, 150, enemy_image_two, 140, 70, 100, 2)

gun = weapon.Weapon(gun_image, 50, 50)

text = pygame.font.Font(None, 60)
text_image = text.render('Score:', True, (0, 0, 0))

loocking_right = True
clock = pygame.time.Clock()
game = True
while game:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pressed = pygame.key.get_pressed()

    delta_x = 0
    delta_y = 0

    if pressed[pygame.K_w]:
        delta_y -= constants.SPEED
        player.movement(0, delta_y)

    if pressed[pygame.K_s]:
        delta_y += constants.SPEED
        player.movement(0, delta_y)

    if pressed[pygame.K_d]:
        delta_x += constants.SPEED
        player.movement(delta_x, 0)
        if loocking_right:
            player.image = pygame.transform.flip(player.image, True, False)
            loocking_right = False

    if pressed[pygame.K_a]:
        delta_x -= constants.SPEED
        player.movement(delta_x, 0)
        if not loocking_right:
            player.image = pygame.transform.flip(player.image, True, False)
            loocking_right = True

    if pressed[pygame.K_SPACE]:
        new_bullet = bullet.Bullet(gun, shot_image, 15, 50, 50)
        ammu.append(new_bullet)       
        
    if player.shape.x > (window.get_width() - player.shape.width - 40):
        player.shape.x = window.get_width() - player.shape.width - 40

    if player.shape.x < 35:
        player.shape.x = 35

    if player.shape.y > (window.get_height() - player.shape.height - constants.EDGE):
        player.shape.y = window.get_height() - player.shape.height - constants.EDGE

    if player.shape.y < 80:
        player.shape.y = 80

    for i in walls:
        if player.shape.colliderect(i.rect):
            player.shape.x = player.shape.x - delta_x
            player.shape.y = player.shape.y - delta_y
            break

    enemie1.update()
    enemie2.update()
    enemie3.update()
    gun.update(player)

    window.fill((0,0,0))
    window.blit(background, (0, 0))
    window.blit(text_image, (20, 20))               

    enemie1.draw(window)
    enemie2.draw(window)
    enemie3.draw(window)
    player.draw(window)
    gun.draw(window)

    for i in ammu:
        i.update()
        
    for i in ammu:
        i.draw(window)

    #for wall in walls:
        #pygame.draw.rect(window, (255, 0, 0), wall.rect)

    pygame.display.update()

pygame.quit()