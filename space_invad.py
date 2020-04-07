import pygame
import random
pygame.init()  # initialising game window
# creating game window#width adn height
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")  # to change window caption
game_icon = pygame.image.load('war.png')
pygame.display.set_icon(game_icon)
player_icon = pygame.image.load('airplane.png')
corX = 368
corY = 536
corX_change = 0
enemy_icon = pygame.image.load('alien.png')
enemyX = random.randint(0, 768)
enemyY = 34
enem_change = random.choice([-3, 3])
background = pygame.image.load('back.png')


def player(x, y):
    screen.blit(player_icon, (x, y))  # to print something on screen


def enemy(x, y):
    screen.blit(enemy_icon, (x, y))


run = True
while run:
    # screen.fill((0, 0, 0))  # rgb color
    screen.blit(background, (0, 0))

    for event in pygame.event.get():  # loop through  all events
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # this checks if key is pressed on keyboard
            if event.key == pygame.K_RIGHT:
                corX_change = 7
            if event.key == pygame.K_LEFT:
                corX_change = -7
        if event.type == pygame.KEYUP:  # check if key
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                corX_change = 0
    corX += corX_change
    if corX >= 736:
        corX -= 8
    elif corX <= 0:
        corX += 8
    enemyX += enem_change

    if enemyX >= 768:  # checeking right boundary hit
        enem_change = -3
        enemyY += 30

    elif enemyX <= 0:  # checking left boundary hit
        enem_change = 3
        enemyY += 30
    player(corX, corY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # update the game screen
