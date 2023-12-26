import pygame
from settings import *

class Tiles(pygame.sprite.Sprite):
	def __init__(self,pos,sprite_group,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
		super().__init__(sprite_group)
		self.sprite_type = sprite_type
		self.image = surface
		
		if sprite_type == "Objects":
			self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
		else:
			#creates a slight offset on players y colliders
			self.rect  = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)
