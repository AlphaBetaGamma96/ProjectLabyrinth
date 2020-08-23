import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#init pygame
pygame.init()
pygame.mixer.init() #init audio

#create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock() #create clock to manage FPS

all_sprites = pygame.sprite.Group() #creates new group (add all sprites to this)

#Game loop
running = True
while running:
    #keep loop running at the same speed
    clock.tick(FPS)

    #grab all events
    for event in pygame.event.get():
        #check if window closed
        if(event.type == pygame.QUIT):
            running = False

    #update
    all_sprites.update()

    #render screen
    screen.fill(BLACK)
    all_sprites.draw(screen)

    #after drawing assets
    pygame.display.flip()

pygame.quit() #when exiting game loop, kill pygame
