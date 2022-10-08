import pygame
from  player import *

class Weapon(pygame.sprite.Sprite):
	def __init__(self,player,groups):
		super().__init__(groups)
		
		state = player.state.split("_")[0]
		player_direction = player.current_direction
		
		self.sprite_type = 'weapon'
		
		#rendering/graphics
		fullpath = f"Graphics/weapons/{player.weapon}/{state}.png"
		self.image = pygame.image.load(fullpath).convert_alpha()
		
		#weapon placement
		#draws weapon based on player direction
		if player_direction == "up":
			self.rect = self.image.get_rect(midbottom = player.rect.midtop -pygame.math.Vector2(16,0))
		elif player_direction == "down":
			self.rect = self.image.get_rect(midtop = player.rect.midbottom-pygame.math.Vector2(16,0))
		elif player_direction == "left":
			self.rect = self.image.get_rect(midright = player.rect.midleft+pygame.math.Vector2(0,16))
		elif player_direction == "right":
			self.rect = self.image.get_rect(midleft = player.rect.midright+pygame.math.Vector2(0,16))
			
			
	