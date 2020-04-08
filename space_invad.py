import pygame
import random
import math
from pygame import mixer  # needed to handle music


class player_begin:
    def __init__(self, x, y, change):
        self.x = x
        self.y = y
        self.change = change


class enemy_begin:
    def __init__(self, index, x, y, changeX):
        self.index = index
        self.x = x
        self.y = y
        self.change = changeX


class bullet_begin:
    def __init__(self, x, y, changeX, changeY, state):
        self.x = x
        self.y = y
        self.changeX = changeX
        self.changeY = changeY
        self.state = state


pygame.init()  # initialising game window
# creating game window#width adn height
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")  # to change window caption
game_icon = pygame.image.load('war.png')
player_icon = pygame.image.load('airplane.png')
enemy_icon = pygame.image.load('alien.png')
background = pygame.image.load('back.png')
bulletimg = pygame.image.load('bullet1.png')
pygame.display.set_icon(game_icon)
mixer.music.load('back.wav')
mixer.music.play(-1)
player = player_begin(368, 536, 0)
enemy = []
for i in range(10):
    enemy.append(enemy_begin(i, random.randint(0, 760), random.randint(
        32, 100), random.choice([-5, -3, 3, 5])))

bullet = bullet_begin(0, 531, 0, -15, 'ready')
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score():
    scorex = font.render("Score :"+str(score), True, (255, 255, 255))
    screen.blit(scorex, (10, 10))


def player_display(x, y):
    screen.blit(player_icon, (x, y))  # to print something on screen


def enemy_display(x, y):
    screen.blit(enemy_icon, (x, y))


def bullet_fly(x, y):
    screen.blit(bulletimg, (x, y))


def check_game_over(enemy):
    for i in range(10):
        if enemy[i].y > 528:
            for j in range(10):
                enemy[j].y = 1500
            font = pygame.font.Font('freesansbold.ttf', 40)
            over_screen = font.render(
                "Game Over!! Score :"+str(score), True, (255, 255, 255))
            screen.blit(over_screen, (210, 250))
            break


def check_collision(x1, y1, x2, y2):
    distance = math.sqrt((int(y2-y1)**2)+(int(x2-x1)**2))
    if int(distance) in range(25):
        return True
    else:
        return False


def after_collision(bullet, enemy):
    collision_sound = mixer.Sound('explo.wav')
    collision_sound.play()
    bullet.state = 'ready'
    bullet.y = 531
    enemy[i].x = random.randint(0, 768)
    enemy[i].y = random.randint(32, 100)
    enemy[i].change = random.choice([-5, -3, 3, 5])
    global score
    score += 1


run = True
while run:
    # screen.fill((0, 0, 0))  # rgb color
    screen.blit(background, (0, 0))
    for event in pygame.event.get():  # loop through  all events
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # this checks if key is pressed on keyboard
            if event.key == pygame.K_RIGHT:
                player.change = 7
            if event.key == pygame.K_LEFT:
                player.change = -7
            if event.key == pygame.K_SPACE:
                if(bullet.state == 'ready'):
                    bullet_sound = mixer.Sound('bullet.wav')
                    bullet_sound.play()
                    bullet.x = player.x+16
                    bullet.state = 'run'

        if event.type == pygame.KEYUP:  # check if key
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.change = 0

    player.x += player.change
    if player.x >= 736:
        player.x -= 8
    elif player.x <= 0:
        player.x += 8
    check_game_over(enemy)
    for i in range(10):
        enemy[i].x += enemy[i].change
        if enemy[i].x >= 768:  # checeking right boundary hit
            enemy[i].change = -3
            enemy[i].y += 60

        elif enemy[i].x <= 0:  # checking left boundary hit
            enemy[i].change = 3
            enemy[i].y += 60
        enemy_display(enemy[i].x, enemy[i].y)
    player_display(player.x, player.y)
    show_score()

    for i in range(10):
        if(check_collision(enemy[i].x, enemy[i].y, bullet.x, bullet.y)):
            after_collision(bullet, enemy)
    if bullet.y < 0:
        bullet.state = 'ready'
        bullet.y = 531
    if bullet.state == 'run':
        bullet.y += bullet.changeY
        bullet_fly(bullet.x, bullet.y)
    pygame.display.update()  # update the game screen
