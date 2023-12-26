import pygame
from settings import *
from particles import *

from random import randint

class Player_magic:
	
	def __init__(self,animator):
		
		self.animator = animator
		
	def cast_heal(self,player,strength,mana_cost,group,cast_sound):
		
		sfx = pygame.mixer.Sound(cast_sound)
		
		if player.mana >= mana_cost:
			pygame.mixer.Sound.play(sfx)
			self.animator.create_particle("aura",player.rect.center,group)
			player.health += strength
			player.mana -= mana_cost
			if player.health > player.base_stats["health"]:
				player.health = player.base_stats["health"]
				
				self.animator.create_particle("heal",player.rect.center,group)
		
	
	def cast_fire(self,player,mana_cost,group,cast_sound):
		
		sfx = pygame.mixer.Sound(cast_sound)
		if player.mana >= mana_cost:
			player.mana -= mana_cost
			pygame.mixer.Sound.play(sfx)
			
			if player.current_direction == 'up':
				direction = pygame.math.Vector2(0,-1)
				
			elif player.current_direction == "down":
				direction = pygame.math.Vector2(0,1)
			
			
			elif player.current_direction == "left":
				direction = pygame.math.Vector2(-1,0)
				
			else:
				direction = pygame.math.Vector2(1,0)
				
			
			
			for i in range(1,6):
				if direction.x:
					offset_x = (direction.x * i) * TILESIZE
					x = player.rect.centerx + offset_x + randint(-TILESIZE // 3,TILESIZE // 3)
					y = player.rect.centery + randint(-TILESIZE // 3,TILESIZE // 3)
					self.animator.create_particle('flame',(x,y),group)
					
					
				elif direction.y:
					offset_y = (direction.y * i) * TILESIZE
					x = player.rect.centerx + randint(-TILESIZE // 3,TILESIZE // 3)
					y = player.rect.centery + offset_y + randint(-TILESIZE // 3,TILESIZE // 3)
					self.animator.create_particle('flame',(x,y),group)
							
				
					
				
				
				
				
			
			
		
		
		
	
	
