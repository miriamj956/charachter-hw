import pygame
import time

pygame.init()

screen = pygame.display.set_mode((600,337))
player = pygame.image.load("plane.png")
bkg = pygame.image.load("sky.jpg")

player_x = 100
player_y = 10

keys = [False, False, False, False]

while player_y < 400:
    screen.blit(bkg,(0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.update()
    #will help to fetch all the events(must put)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_DOWN:
                keys[2] = True
            if event.key == pygame.K_LEFT:
                keys[1] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_DOWN:
                keys[2] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False

    if keys[0]: #keys[0] == True
        if player_y > 0:
            player_y -=7
    if keys[2]:
        if player_y < 500:
            player_y +=7
    if keys[1]:
        if player_x > 0:
            player_x -=7
    if keys[3]:
        if player_x < 500:
            player_x +=7
    player_y += 5 #makes the player constantly go down
    time.sleep(0.05) #makes player go slower (otherwise will go very fast)
print("Game Over!")

