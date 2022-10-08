import pygame
from math import sin
class Entity(pygame.sprite.Sprite):
	
	def __init__(self,groups):
		super().__init__(groups)
		
		self.frame_index = 0
		self.animation_time = 1 / 4
		self.direction = pygame.math.Vector2()
		
			         
	def movement(self,speed):
		
		self.rect.center += self.direction * speed
		self.hitbox.x += self.direction.x * speed
		self.CheckCollisions("Horizontal")
		self.hitbox.y += self.direction.y * speed
		self.CheckCollisions("Vertical")
		self.rect.center = self.hitbox.center
		
	def wave_value(self):
		
		# hitflash value
		value = sin(pygame.time.get_ticks())
		if value >= 0: return 255
		else: return 0
			
		
		
		
		
	def CheckCollisions(self,direction):
		
		# checks the player direction first then if it collided with a collision sprite it puts its center of the object to the opposite side of direction based on inputs
		
		if direction == "Horizontal":
			for sprite in self.collision_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x >0: #moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x <0: #moving left
						self.hitbox.left = sprite.hitbox.right
					
						
					
		if direction == "Vertical":
			for sprite in self.collision_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y >0: #moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y <0: #moving up
						self.hitbox.top = sprite.hitbox.bottom
						
	
	