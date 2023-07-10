import pygame
from Settings import *

class Item:
	
	def __init__(self,l,t,w,h,selection_index,font):
		self.rect = pygame.Rect(l,t,w,h)
		
		self.index = selection_index
		self.font = font
		
	def display_names(self,surface,name,cost,selected):
		
		color = Textcolor_selected if selected else Text_color
		#title display
		title_surf = self.font.render(name,False,color)
		title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))
		# cost display 
		cost_surf = self.font.render(f"{int(cost)}",False,color)
		cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))
		
		surface.blit(title_surf,title_rect)
		
		surface.blit(cost_surf,cost_rect)
		
		
	def display_bar(self,surface,value,max_value,selected):
		
		top = self.rect.midtop + pygame.math.Vector2(0,60)
		bottom = self.rect.midbottom - pygame.math.Vector2(0,60)
		color = Bar_colorselected if selected else Bar_color
		
		#setup
		full_height = bottom[1] - top[1]
		relative_number = (value/max_value) * full_height
		value_rect = pygame.Rect(top[0] - 15 ,bottom[1] - relative_number,30,10)

		#rendering the lines
		
		pygame.draw.line(surface,color,top,bottom,5)
		pygame.draw.rect(surface,color,value_rect)
		
	def trigger(self,player):
		
		upgrade_attribute = list(player.base_stats.keys())[self.index]
		
		if player.exp >= player.upgrade_cost[upgrade_attribute]:
			player.exp -= player.upgrade_cost[upgrade_attribute]
			
			#increases the base stat and also raises its upgradee cost
			player.base_stats[upgrade_attribute] *= 1.2	
			player.upgrade_cost[upgrade_attribute] *= 1.4
		
		
		if player.base_stats[upgrade_attribute] >= player.max_stats[upgrade_attribute]:
			
			player.base_stats[upgrade_attribute] = player.max_stats[upgrade_attribute]
			
			
			
			
	def display(self,surface,selection_num,name,value,max_value,cost):
		
		if self.index == selection_num:
			
			pygame.draw.rect(surface,Upgrade_bgcolor_selected,self.rect)
			pygame.draw.rect(surface,UI_bgcolor,self.rect,4)
		
		
		else:
			pygame.draw.rect(surface,UI_bgcolor,self.rect)
			pygame.draw.rect(surface,UI_bgcolor,self.rect,4)
			
		self.display_names(surface,name,cost,self.index == selection_num)
		
		self.display_bar(surface,value,max_value,self.index == selection_num)
	
	
