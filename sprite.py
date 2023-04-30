from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,image_name, x, y, width, height, speed):

        self.image1 = transform.scale(image.load('kokohen.png'),(width, height))
        self.image = transform.scale(image.load(image_name),(width, height))

        self.image2 = transform.scale(image.load("kokohen_2.png"),(width, height))
        self.rect = self.image1.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] == True and self.rect.x != 5:
            self.rect.x = self.rect.x - self.speed  
            self.image = self.image1
        elif keys[K_RIGHT] == True and self.rect.x != 645:
            self.rect.x = self.rect.x + self.speed
            self.image = self.image2

class Egg(GameSprite):
    def update(self, window):
        self.rect.y = self.rect.y + self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = randint(0,80)
            self.rect.x = randint(50,650)
            self.speed = randint(1,2)    
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    


