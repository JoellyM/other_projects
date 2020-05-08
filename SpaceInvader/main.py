import pygame
import random
import math
from pygame import mixer

# Initianize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Space-invaders.png')
playerX = 368
playerY = 480
playerX_change = 0

# 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('space-ship.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(20 )
    enemyY_change.append(40)

# Background
Background = pygame.image.load('background.png')

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Bullet

# Ready - You can't see the buillet on the screen
# Fire the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 25
bullet_state = "ready"

# bullet sound
bullet_sound = mixer.Sound('laser.wav')

# Collision sound
explosion_sound = mixer.Sound('explosion.wav')

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

textX = 10
textY = 10

def show_score(x, y):
        score = font.render("Score: " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw on screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Pythagore
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    return False   

# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 59, 89))
    
    # background image
    screen.blit(Background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if a keystroke is pressed check if it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -15
            if event.key == pygame.K_RIGHT:
                playerX_change = 15
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change

    if playerX >= 736:
        playerX = 736
    if playerX <= 0:
        playerX = 0


    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Enemy movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bullet_sound.play()
        bulletY -= bulletY_change

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] >= 736:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -15
        elif enemyX[i] <= 0:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 15

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision and bullet_state == "fire":
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 200)

        enemy(enemyX[i], enemyY[i], i)

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
