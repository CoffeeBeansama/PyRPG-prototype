import pygame
from settings import *
from entity import Entity
from Support import *
from debug import debug
from PlayerUI import UI




class Enemy(Entity):
	def __init__(self,name,pos,groups,collision_sprites,damage_player,trigger_death_type):
		
		  # setup
		  super().__init__(groups)
		  self.sprite_type = "enemy"
		  
		  
		  #graphics
		  self.import_graphics(name)
		  self.state = "idle"
		  self.image = self.animation[self.state][self.frame_index]
		  
		  #movement
		  self.rect = self.image.get_rect(topleft = pos)
		  self.hitbox = self.rect.inflate(0,-10)
		  self.collision_sprites = collision_sprites
		  
		  #enemy properties
		  
		  self.name = name
		  monster_info = enemy_data[self.name]
		  self.health = monster_info["health"]
		  self.exp = monster_info["exp"]
		  self.speed = monster_info["speed"]
		  self.attack_damage = monster_info['damage']
		  self.knockback = monster_info['knockback']
		  self.attack_radius = monster_info["attack_radius"]  
		  self.patrol_radius = monster_info['patrol_radius']
		  self.attack_type = monster_info['attack_type']
		  self.attack_sound = monster_info["attack_sfx"]
		  self.death_sound = "audio/death.wav"
		  self.playerdeath_sfx = "audio/player_hit.wav"
		  
		  #player interaction
		  self.can_attack = True
		  self.attack_cooldown = 600
		  self.attack_time = 0
		  self.damage_player = damage_player
		  self.trigger_death_animation = trigger_death_type
		  
		  #invincibility timer
		  
		  self.vulnerable = True
		  self.hit_time = 0
		  self.invincibility_frames = 600
		  
		  self.alive = True
		  self.ui = UI()
		  
		  	
		  
	
	def import_graphics(self,monster_name):
		    self.animation = {"idle":[],"move":[],"attack":[]}
		    main_path = f"Graphics/monsters/{monster_name}/"
		    
		    for animation in self.animation.keys():
		    	self.animation[animation] = import_folder(main_path + animation)
	
	
	def get_player_distance_direction(self,player):
		enemy_vec = pygame.math.Vector2(self.rect.center)
		player_vec = pygame.math.Vector2(player.rect.center)
		distance = (player_vec - enemy_vec).magnitude()
		
		if distance > 0:
			direction = (player_vec - enemy_vec).normalize()
		else:
			direction = pygame.math.Vector2()
			
			
		
		return (distance,direction)
	
	def cooldowns(self):
		
		current_time = pygame.time.get_ticks()
		
		if not self.can_attack:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.can_attack = True
				
		
		#Iframes cooldown
		if not self.vulnerable:
			if current_time - self.hit_time >= self.invincibility_frames:
				self.vulnerable = True
	
	
			
		
	def get_state(self,player):
		distance = self.get_player_distance_direction(player)[0]
		
		#player inside attack radius
		if distance <= self.attack_radius and self.can_attack:
			if self.state != "attack":
				self.frame_index = 0
				self.state = "attack"
				self.damage_player(self.attack_damage,self.attack_type,self.attack_sound,self.playerdeath_sfx)
			
		
		#player inside patrol radius
		elif distance <= self.patrol_radius:
			self.state = "move"
		
		#player outside patrol radius
		else: self.state = 'idle'
		
	def actions(self,player):
			if self.state == 'attack':
				  self.attack_time = pygame.time.get_ticks()	
			elif self.state == 'move':
				self.direction = self.get_player_distance_direction(player)[1]
			else:  self.direction = pygame.math.Vector2()
			
	def animate(self):
					
		#increments the frame index when receiving input 
		#when frame index reaches to maximum it loops over again to repeat the animation cycle
		
		animation = self.animation[self.state]
		self.frame_index += self.animation_time
		
		if self.frame_index >= len(animation):
			if self.state == "attack":
				self.can_attack = False
			self.frame_index = 0
		
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center=self.hitbox.center)
		
	def take_damage(self,player,attack_type,sfx):
				
				enemyhit = pygame.mixer.Sound(sfx)
				self.direction = self.get_player_distance_direction(player)[1]
			
					
				if self.vulnerable:
					if attack_type == "weapon":		
								
						#weapon  damage
						self.health -= player.player_full_damage()
						pygame.mixer.Sound.play(enemyhit)
						self.hit_time = pygame.time.get_ticks()
						self.vulnerable = False
					
					else:
						self.health -= player.magic_damage()
						
	
			
					
					
					
					
	def check_if_alive(self,player,exp_gained,sfx):
		
		deathsound = pygame.mixer.Sound(sfx)
		#applies if no hp left 
		if self.health <= 0:
			self.alive = False
			pygame.mixer.Sound.play(deathsound)
			self.trigger_death_animation(self.rect.center,self.name)
		
		if not self.alive:
		  	self.ui.increase_exp(player,exp_gained)
		  	self.kill()
		  	
			
			
	def hit_reaction(self):
		
		#applies knockback and hitflash
		if not self.vulnerable:
			alpha = self.wave_value()
			self.image.set_alpha(alpha)
			self.direction *= -self.knockback
		else:
			self.image.set_alpha(255)
						
			
		
			
	def update(self):
	 	
	 	 self.hit_reaction()
	 	 self.cooldowns()
	 	 self.movement(self.speed)
	 	 self.animate()
	 	 
		  
	def enemy_update(self,player):
		  
		  self.check_if_alive(player,self.exp,self.death_sound) 		
		  self.get_state(player)
		  self.actions(player)
		  
		  
		  
		  
		  
		  
		      
	
	
	
