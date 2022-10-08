import pygame
from Settings import *
from debug import debug
from item import Item


class Upgrade:
	
	
	def __init__(self,player):
		
		
		#general setup
		self.surface = pygame.display.get_surface()
		self.player = player 
		self.attribute_number = len(player.base_stats)
		self.attribute_names = list(player.base_stats.keys())
		self.max_values = list(self.player.max_stats.values())
		
		self.font = pygame.font.Font(UI_font,UI_fontsize)
		
		
		#item instances dimensions
		self.height = self.surface.get_size()[1] * 0.8
		self.width =  self.surface.get_size()[0] // 6
		self.create_items()
		
		
		self.selection_index = 0
		self.selection_time = 0
		self.can_move_selection = True
		

		self.Up_image = pygame.image.load("Graphics/Buttons/Up.png")
		self.Left_image = pygame.image.load("Graphics/Buttons/Left.png")
		self.Right_image = pygame.image.load("Graphics/Buttons/Right.png")
	
	def get_inputs(self):
			
			pos = pygame.mouse.get_pos()
			Up_button = self.surface.blit(self.Up_image,(1000,350))
			Left_button = self.surface.blit(self.Left_image,(870,450))
			Right_button = self.surface.blit(self.Right_image,(1130,450))
			
			
			if self.can_move_selection:
				if Up_button.collidepoint(pos):
					self.can_move_selection = False
					self.item_list[self.selection_index].trigger(self.player)
					self.selection_time = pygame.time.get_ticks()
					
					pygame.mouse.set_pos(0,0)
					
					
				elif Left_button.collidepoint(pos) and self.selection_index >= 1:
					self.selection_index -= 1
					self.can_move_selection = False
					self.selection_time = pygame.time.get_ticks()
					pygame.mouse.set_pos(0,0)
					
				elif Right_button.collidepoint(pos) and self.selection_index < self.attribute_number - 1:
					self.selection_index += 1
					self.can_move_selection = False
					self.selection_time = pygame.time.get_ticks()
					pygame.mouse.set_pos(0,0)
	
	
	def create_items(self):
		self.item_list = []
		
		for item,index in enumerate(range(self.attribute_number)):
			#horizontal position
			
			full_width = self.surface.get_size()[0]
			increment = full_width // self.attribute_number
			left = (item * increment) + (increment - self.width) // 2
			#vertical position
			top = self.surface.get_size()[1] * 0.1
			item = Item(left,top,self.width,self.height,index,self.font)
			self.item_list.append(item)
	def selection_cooldown(self):
		if not self.can_move_selection:
				current_time = pygame.time.get_ticks()
				if current_time - self.selection_time >= 100:
					self.can_move_selection = True
					
				
	def display(self):
		
		self.get_inputs()
		self.selection_cooldown()
		
		#get player attributes
		
		for index,item in enumerate(self.item_list):
			
			name = self.attribute_names[index]
			value = self.player.get_value_byindex(index)
			max_value = self.max_values[index]
			cost = self.player.get_cost_byindex(index)
			
			item.display(self.surface,self.selection_index,name,value,max_value,cost)
			
		self.get_inputs()
			
