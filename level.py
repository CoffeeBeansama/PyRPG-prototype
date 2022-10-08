import pygame,sys	
from  Settings import *
from tiles import Tiles
from player import Player
from debug import debug
from Support import *
from random import choice, randint
from weapon import Weapon
from PlayerUI import UI
from enemy import Enemy
from particles import Animate
from magic import Player_magic
from time import sleep
from upgrade import Upgrade
from pygame import mixer


class YsortCameraGroup(pygame.sprite.Group):
		
		def __init__(self):
			
			super().__init__()
			self.display_canvas = pygame.display.get_surface()
			self.half_width = self.display_canvas.get_size()[0] // 2
			self.half_height = self.display_canvas.get_size()[1] // 2
			self.offset = pygame.math.Vector2()
			
			# creating the floor
			self.floor_surface = pygame.image.load("Graphics/tilemap/ground.png").convert()
			self.floor_rect = self.floor_surface.get_rect(topleft =(0,0))
			
		def enemy_update(self,player):
			enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy'] 
			for enemy in enemy_sprites:
				enemy.enemy_update(player)
				
				
			
			
		
		def custom_draw(self,player):
			
			#getting the offset  for camera
			self.offset.x = player.rect.centerx - self.half_width
			self.offset.y = player.rect.centery - self.half_height
			
			# rendering floors
			
			floor_offset_pos = self.floor_rect.topleft - self.offset
			self.display_canvas.blit(self.floor_surface,floor_offset_pos)
			
			for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
				offset_rect = sprite.rect.topleft - self.offset
				self.display_canvas.blit(sprite.image,offset_rect)
				
				
				
class Level:
	def __init__(self):
		
		self.display_canvas = pygame.display.get_surface()
		
		# sprites setup
		self.visible_sprites = YsortCameraGroup()
		self.collision_sprites = pygame.sprite.Group()
		
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		self.title_image = pygame.image.load('Title.png')
		self.start_image = pygame.image.load("Button.png")
		self.setting_image = pygame.image.load("Graphics/Buttons/Settings.png")
		
		
		
		self.create_map()
		
		
		self.ui = UI()
		self.uprade_menu = Upgrade(self.player)
		
		#particles
		
		self.particle_animation = Animate()
		self.player_magic = Player_magic(self.particle_animation)
		
		self.start_level = False
		self.current_weapon = None
		
		self.playerhit_sfx = "audio/sword.wav"
		self.heal_sfx = "audio/heal.wav"
		self.fire_sfx = "audio/Fire.wav"
		
		mixer.music.load("audio/main_menu.ogg")
			
		mixer.music.play(-1)
		
		
		# map creation
		
	def unpause_game(self):
		
		pygame.mouse.set_pos(0,0)
		
		
		sleep(1)
		
		
		pos = pygame.mouse.get_pos()
		Settings_button = self.screen.blit(self.setting_image,(10,150))
		
		
		game_paused = self.player.display_menu and Settings_button.collidepoint(pos)
		if game_paused:
			pygame.mouse.set_pos(0,0)
			self.player.display_menu = False
			
			
	
	def create_weapon(self):
		self.current_weapon = Weapon(self.player,[self.visible_sprites,self.attack_sprites])
		
	
	def destroy_weapon(self):
			if self.current_weapon:
				self.current_weapon.kill()
			self.current_weapon = None
			
	def cast_magic(self,style,strength,mana_cost):
		
		
		if style == "heal":
			self.player_magic.cast_heal(self.player,strength,mana_cost,[self.visible_sprites],self.heal_sfx)
			
		if style == "flame":
			self.player_magic.cast_fire(self.player,mana_cost,[self.visible_sprites,self.attack_sprites],self.fire_sfx)

		
	def destroy_magic(self):
		pass
	def create_grass_effect(self):
		pass
		
	def player_attack_logic(self,sfx):
		
		
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				#checks collision with all attackable sprites
				collision_sprite = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				
				#if it finds an attackble sprite upon collision it does the logics below
				if collision_sprite:
					for target_sprite in collision_sprite:
						if target_sprite.sprite_type == "grass":
							
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0,75)
							for leaf in range(randint(3,6)):
								self.particle_animation.create_grass_particle(pos - offset,[self.visible_sprites])
							target_sprite.kill()
						
							
						else: target_sprite.take_damage(self.player,attack_sprite.sprite_type,sfx)
						
						
	def trigger_death_animation(self,pos,particle_type):
						
		self.particle_animation.create_particle(particle_type,pos,self.visible_sprites)
						
						
	
	def create_map(self):
		
		#map layout imports
		layouts = {
				"boundary": import_csv_layout("Map/map_FloorBlocks.csv"),
				"grass": import_csv_layout("Map/map_Grass.csv"),
				"object": import_csv_layout("Map/map_Objects.csv"),
				"entities": import_csv_layout("Map/map_Entities.csv")
		}
		props = {
				"grass": import_folder("Graphics/grass/"),
				"Large_objects": import_folder("Graphics/objects/")
		
		}
	
		for style,layout in layouts.items():
			for row_index, row in enumerate(layout):
				for column_index, column in enumerate(row):
						
						if column != "-1":
							x = column_index * TILESIZE
							y = row_index * TILESIZE
							
							#creates boundaries
							if style == "boundary":
								Tiles((x,y),self.collision_sprites,"Invisible")
							
							#spawns grass
							if style == "grass":
								pass
							
								#random_grass = choice(props["grass"])
								#Tiles((x,y),[self.visible_sprites,self.collision_sprites,self.attackable_sprites],"grass",random_grass)
								
							#spawns object
							if style == "object":
								pass
								#obj = props["Large_objects"][int(column)]
								#Tiles((x,y),[self.visible_sprites,self.collision_sprites],"Objects",obj)
							
							
						
							
							if style == "entities":
								if column == "394":
									pass
								elif column == "392":
									monster_name = "raccoon"
								elif column == "391":
									monster_name = "spirit"
								elif column == "393":
									monster_name = "squid"
								else: monster_name = "bamboo"
								Enemy(monster_name,(x,y),[self.visible_sprites,self.attackable_sprites],self.collision_sprites,self.damage_player,self.trigger_death_animation)
								
										
									
									
								
		
		#spawns the player
		#player properties
		self.player = Player((1750,2000),
		[self.visible_sprites],
		self.collision_sprites,
		self.create_weapon,
		self.destroy_weapon,
		self.cast_magic,
		
		)
		
	def damage_player(self,damage,attack_type,hit_sfx,death_sfx):
				
				hit = pygame.mixer.Sound(hit_sfx)
				death = pygame.mixer.Sound(death_sfx)
				
				
				if self.player.health > 1:
					if self.player.vulnerable:
						pygame.mixer.Sound.play(hit)
						self.player.health -= damage
						self.player.vulnerable = False
						self.player.hurt_time = pygame.time.get_ticks()
						self.particle_animation.create_particle(attack_type,self.player.rect.center,[self.visible_sprites])
						
				else:
					pygame.mixer.Sound.play(death)
					pygame.quit()
					sys.exit()
	
	
	def upgrade_ui(self):
		pass	
					
				
				
				    
	
	def run(self):
		pos = pygame.mouse.get_pos()
		
		
		if self.start_level:
			
			
			if self.player.display_menu:
				
				
				self.uprade_menu.display()
				self.unpause_game()
				
				
			else:
				
				self.visible_sprites.enemy_update(self.player)
			
				self.visible_sprites.update()
				self.visible_sprites.custom_draw(self.player)
				self.player.Update()
				self.player_attack_logic(self.playerhit_sfx)
				self.ui.display(self.player)
				
		else:
			title = self.screen.blit(self.title_image,(430,100))
			
			start_button = self.screen.blit(self.start_image,(450,350))
			if start_button.collidepoint(pos):
				self.start_level = True
			
		
		
		
		
		



				
			
		
		
		