import pygame
from Settings import *
from debug import debug
from Support import import_folder
from entity import Entity

class Player(Entity):
	def __init__(self,pos,sprite_group,obstacle_sprites,create_weapon,destroy_weapon,cast_magic):
		super().__init__(sprite_group)
		
		#rendering/graphics
		self.image = pygame.image.load("Graphics/test/player.png").convert_alpha()
		self.rect  = self.image.get_rect(topleft = pos)
		self.collision_sprites = obstacle_sprites
		
		self.Up_image = pygame.image.load("Graphics/Buttons/Up.png")
		self.Down_image = pygame.image.load("Graphics/Buttons/Down.png")
		self.Left_image = pygame.image.load("Graphics/Buttons/Left.png")
		self.Right_image = pygame.image.load("Graphics/Buttons/Right.png")
		
		self.melee_image = pygame.image.load("Graphics/Buttons/melee.png")
		self.magic_image = pygame.image.load("Graphics/Buttons/magic.png")
		
		self.melee_weaponchange_image = pygame.image.load("Graphics/Buttons/MeleeWeaponChange.png")
		self.import_player_assets()
		
		self.magic_weaponchange_image = pygame.image.load("Graphics/Buttons/MagicWeaponChange.png")
		
		self.setting_image = pygame.image.load("Graphics/Buttons/Settings.png")
		
		
		self.import_player_assets()
		
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		self.hitbox = self.rect.inflate(0,-26)
		
		
		#movement
		self.state  = "down_idle"
		self.current_direction = "down"
		self.button_clicked = False
		

		#attacks
		self.attacking = False
		self.attack_cooldown = 300
		self.attack_time = 0
		
		#weapons
		self.create_weapon = create_weapon
		self.weapon_index = 0
		self.weapon = list(weapon_data.keys())[self.weapon_index]
		self.destroy_weapon = destroy_weapon
		self.can_switch_weapon = True
		self.weapon_switch_time = 0
		self.weapon_switch_cooldown = 300
		self.weapon_data = weapon_data
		
		
		
		#magic
		self.cast_magic = cast_magic
		
		self.magic_index = 0
		self.magic = list(magic_data.keys())[self.magic_index]
		self.can_switch_magic = True
		self.magic_switch_time = 0
		self.magic_switch_cooldown = 300
		self.magic_data = magic_data
		

		
		#player stats
		
		self.base_stats = {"health" : 100, "mana":60,"attack":10, "magic": 4, "speed": 20}
		
		self.max_stats = {"health" : 300, "mana":140,"attack":20, "magic": 10, "speed": 30}
		
		self.upgrade_cost = {"health" : 100, "mana":100,"attack":100, "magic": 100, "speed": 100}
		self.health = self.base_stats["health"] * 0.8
		self.mana = self.base_stats["mana"] * 0.8
		self.exp = 300
		
		self.display_menu = False
		self.vulnerable = True
		self.hurt_time = 0
		
		self.invincibility_frame = 600
	
	
				
	def import_player_assets(self):
		
		player_path = "Graphics/player/"
		
		self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]
		}
		
		for animation in self.animations.keys():
			full_path  = player_path + animation
			self.animations[animation] = import_folder(full_path)
		print(self.animations)
		
		
	def get_states(self):
		
		if self.direction.x == 0 and self.direction.y == 0:
			if not "idle" in self.state and not "attack" in self.state:
				self.state = self.state + "_idle"
				
		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			
	 
	
	#cooldown
	def cooldowns(self):
		
		current_time = pygame.time.get_ticks()
		#checks if attacking and reverts back to idle state and checks where is player is facing
		switch_weapon_tick = current_time - self.weapon_switch_time >= self.weapon_switch_cooldown + weapon_data[self.weapon]['cooldown']
		
		switch_magic_tick = current_time - self.magic_switch_time >= self.magic_switch_cooldown 
		
		
		if not self.can_switch_weapon:
			if switch_weapon_tick:
				self.can_switch_weapon = True
				pygame.mouse.set_pos(0,0)
				
		if not self.can_switch_magic:
			if switch_magic_tick:
				self.can_switch_magic = True
				pygame.mouse.set_pos(0,0)
				
		if not self.vulnerable:
			alpha = self.wave_value()
			self.image.set_alpha(alpha)
	
			if current_time - self.hurt_time >= self.invincibility_frame:
				
				self.vulnerable = True
		else: self.image.set_alpha(255)
			
		
		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
			         self.attacking = False
			         self.destroy_weapon()
			         
			         pygame.mouse.set_pos(0,0)
			         if self.current_direction == "up":
			         	self.state = "up_idle"
			         elif self.current_direction == "down":
			         	self.state = "down_idle"
			         elif self.current_direction == "left":
			         	self.state = "left_idle"
			         elif self.current_direction == "right":
			         	self.state = "right_idle"
	
	
	def display_settings(self):
		pos = pygame.mouse.get_pos()
		Settings_button = self.screen.blit(self.setting_image,(10,150))
		
		if Settings_button.collidepoint(pos):
			self.display_menu = True
			         	
	
	 
	def  get_value_byindex(self,index):
			         	
		return list(self.base_stats.values())[index]
		
	def get_cost_byindex(self,index):
			         	
		return list(self.upgrade_cost.values())[index]
			         	
	def inputs(self,direction):
		
		if not self.display_menu:
			Up_button = self.screen.blit(self.Up_image,(1000,350))
			Down_button = self.screen.blit(self.Down_image,(1000,550))
			Left_button = self.screen.blit(self.Left_image,(870,450))
			Right_button = self.screen.blit(self.Right_image,(1130,450))
			Melee_button = self.screen.blit(self.melee_image,(50,500))
			Magic_button = self.screen.blit(self.magic_image,(300,500))
			Changeweapon_button = self.screen.blit(self.melee_weaponchange_image,(1170,50))
			Changemagic_button = self.screen.blit(self.magic_weaponchange_image,(1170,150))
		

		
		#render button Ui
		
		pos = pygame.mouse.get_pos()
		
			
		
		#direction input
		#changes direction bas3d on player input
		if not self.attacking:
			if Up_button.collidepoint(pos):
			          	self.current_direction = "up"
			          	direction.y = -1
			          	self.state = "up" 
			elif Down_button.collidepoint(pos):
			          	self.current_direction = "down"
			          	direction.y = 1
			          	self.state = "down"
			          
			else: direction.y = 0
			
			if Left_button.collidepoint(pos):
			        self.current_direction = "left"
			        direction.x = -1
			        self.state = "left"
			elif Right_button.collidepoint(pos):
			        self.current_direction = "right"
			        direction.x = 1
			        self.state = "right"
			        
			else: direction.x = 0
		

	
		#Melee and magic input
		using_weapon = Melee_button.collidepoint(pos) and not self.attacking
		
		if using_weapon:
		          self.attacking = True
		          self.create_weapon()
		          self.attack_time = pygame.time.get_ticks()
		          
		          if self.current_direction == "up":
		          	self.state = "up_attack"
		          elif self.current_direction == "down":
		          	self.state = "down_attack"
		          elif self.current_direction == "left":
		          	self.state = "left_attack"
		          elif self.current_direction == "right":
		         	 self.state = "right_attack"
		
		using_magic = Magic_button.collidepoint(pos) and not self.attacking
		if using_magic:
		          self.attacking = True
		          
		          style = list(magic_data.keys())[self.magic_index]
		          strength = list(magic_data.values())[self.magic_index]["strength"]
		          mana_cost = list(magic_data.values())[self.magic_index]["mana_cost"]
		          
		          self.cast_magic(style,strength,mana_cost)
		          self.attack_time = pygame.time.get_ticks()
		          
		          
		          if self.current_direction == "up":
		          	self.state = "up_attack"
		          elif self.current_direction == "down":
		          	self.state = "down_attack"
		          elif self.current_direction == "left":
		          	self.state = "left_attack"
		          elif self.current_direction == "right":
		          	self.state = "right_attack"
		
		maximum_weapon_capacity = len(list(weapon_data.keys())) -1 
		
		switching_weapon = Changeweapon_button.collidepoint(pos) and self.can_switch_weapon
		if switching_weapon:
		          self.can_switch_weapon = False
		          self.weapon_switch_time = pygame.time.get_ticks()
		          if self.weapon_index < maximum_weapon_capacity:
		          	self.weapon_index += 1
		          else:
		          	self.weapon_index = 0
		          self.weapon = list(weapon_data.keys())[self.weapon_index]
		else:
		      pos = pygame.mouse.get_pos()
		 
		
		maximum_magic_capacity = len(list(magic_data.keys())) -1
		
		switching_magic = Changemagic_button.collidepoint(pos) and self.can_switch_magic
		if switching_magic:
		          self.can_switch_magic = False
		          self.magic_switch_time = pygame.time.get_ticks()
		          if self.magic_index < maximum_magic_capacity:
		          	self.magic_index += 1
		          else:
		          	self.magic_index = 0
		          self.magic = list(magic_data.keys())[self.magic_index]
		else:
		      pos = pygame.mouse.get_pos()
		
		      
	def player_full_damage(self):
			         
		base_damage = self.base_stats["attack"]
		weapon_damage =  weapon_data[self.weapon]['damage']
		
		full_damage = int(base_damage + weapon_damage)
		
		return full_damage 
			        
	
	def animate(self):
		
		#increments the frame index when receiving input 
		#when frame index reaches to maximum it loops over again to repeat the animation cycle
		animation = self.animations[self.state]
		self.frame_index += self.animation_time
		
		if self.frame_index >= len(animation):
			self.frame_index = 0
		
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center=self.hitbox.center)
	
	def update_exp(self,exp_acquired):
		
		updated_exp = int(self.exp + exp_acquired)
		
		return updated_exp
		
	def magic_damage(self):
		base_damage = self.base_stats["magic"]
		strength = magic_data[self.magic]["strength"]
		full_damage = int(base_damage + strength)
		
		return full_damage 
		
	
	
	def mana_recover(self):
		if self.mana < self.base_stats["mana"]:
			self.mana += 0.01 * self.base_stats["magic"]
		else: self.mana = self.base_stats["mana"] - 0.1
		
		
		
	def Update(self):
		self.cooldowns()
		self.display_settings()
		
		if not self.display_menu:
			self.inputs(self.direction)
			
			
		self.movement(self.base_stats["speed"])
		self.get_states()
		self.animate()
		self.mana_recover()
		
		
		