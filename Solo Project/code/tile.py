import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,group,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(group)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'oblect':
            #do an offset
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)