import pygame, sys
import random, time
from pygame.locals import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill("white")
pygame.display.set_caption("Game")
background = pygame.image.load("Lab8/photos/AnimatedStreet.png")
coin = pygame.image.load("Lab8/photos/coin.png")
coint = pygame.transform.scale(coin, (30, 30))

bg_sound = pygame.mixer.Sound("Lab8/sounds/Lectures_G1_Week10_racer_resources_background.wav")
bg_sound.play()

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab8/photos/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab8/photos/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coins(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = coint
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        

P1 = Player()
E1 = Enemy()
C1 = Coins()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.2
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, "black")
    screen.blit(scores, (10, 10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('Lab8/sounds/Lectures_G1_Week10_racer_resources_crash.wav').play()
          time.sleep(1)
                   
          screen.fill("red")
          screen.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    clock.tick(FPS)
    pygame.display.flip()