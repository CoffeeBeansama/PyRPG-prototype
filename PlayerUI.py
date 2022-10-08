import pygame
from Settings import *


class UI:
	def __init__(self):
		
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_font,UI_fontsize)
		
		#bar setup
		self.healthbar_rect = pygame.Rect(10,10,Healthbar_width,Bar_height)
		self.manabar_rect = pygame.Rect(10,34,Manabar_width,Bar_height)
		
		#convert weapon dictionary
		self.weapon_graphics = []
		for weapons in weapon_data.values():
			path = weapons["graphics"]
			weapons = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapons)
			
		self.magic_graphics = []
		for magics in magic_data.values():
			path = magics["graphic"]
			magics = pygame.image.load(path).convert_alpha()
			self.magic_graphics.append(magics)
		
	def show_bar(self,current,max_amount,bg_rect,color):
		
		#drawing background
		pygame.draw.rect(self.display_surface,UI_bgcolor,bg_rect)
		
		#converting health/mana to pixels
		# gets the runtime health and divides it to the maximum health
		# gets the pixel size by width and multiply it to display the runtime health
		ratio = current/max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width
		
		#drawing the actual stat bars
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_bgcolor,bg_rect,3)
	
	def show_exp(self,exp):
		text_surface = self.font.render(str(int(exp)),False,Text_color)
		
		exp_bg_x = 10
		exp_bg_y = 60
		exp_bg_width = 120
		exp_bg_height = 40
		exp_text_x =12
		exp_text_y = 63
		
		pygame.draw.rect(self.display_surface,UI_bgcolor,(exp_bg_x,exp_bg_y,exp_bg_width,exp_bg_height))
		pygame.draw.rect(self.display_surface,UI_bgcolor,(exp_bg_x,exp_bg_y,exp_bg_width,exp_bg_height),3)
		self.display_surface.blit(text_surface,(exp_text_x,exp_text_y))
	
	def selection_box(self,left,top,has_switched):
		bg_rect = pygame.Rect(left,top,Itembox_size,Itembox_size)
		pygame.draw.rect(self.display_surface,UI_bgcolor,bg_rect)
		# flashes yellow when switching
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_bordercolor_active,bg_rect,3)
			
		else:pygame.draw.rect(self.display_surface,UI_bordercolor,bg_rect,3)
		
		return bg_rect
	
	def weapon_overlay_display(self,weapon_index,has_switched):
		bg_rect = self.selection_box(600,600,has_switched)
		
		weapon_image = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_image.get_rect(center = bg_rect.center)
		self.display_surface.blit(weapon_image,weapon_rect)
		
	def magic_overlay_display(self,magic_index,has_switched):
		bg_rect = self.selection_box(700,600,has_switched)
		
		magic_image = self.magic_graphics[magic_index]
		magic_rect = magic_image.get_rect(center = bg_rect.center)
		self.display_surface.blit(magic_image,magic_rect)
		
		
	
	def display(self,player):
		self.show_bar(player.health,player.base_stats["health"],self.healthbar_rect,Health_color)
		self.show_bar(player.mana,player.base_stats["mana"],self.manabar_rect,Mana_color)
		self.show_exp(player.exp)
		self.weapon_overlay_display(player.weapon_index,not player.can_switch_weapon) # weapon
		self.magic_overlay_display(player.magic_index, not player.can_switch_magic) # magic
		
	def increase_exp(self,player,exp_gained):
		player.exp += exp_gained
		
		
		