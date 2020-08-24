import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

#COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    #pygame object to represent sprites
    #inherit pygame.sprite.Sprite
    def __init__(self):
        super(Player, self).__init__()
        #required attributes
        self.image = pygame.Surface((50, 50)) #what it looks like
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()  #rectange that encloses sprite (outer border)
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        self.rect.x += 5
        if(self.rect.left>WIDTH): #if left side of rect of sprite goes pass screen
            self.rect.right=0 #reset to 0


#init pygame
pygame.init()
pygame.mixer.init() #init audio

#create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock() #create clock to manage FPS

all_sprites = pygame.sprite.Group() #creates new group (add all sprites to this)
player = Player()
all_sprites.add(player)

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
