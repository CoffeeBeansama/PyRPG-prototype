import pygame
from Support import import_folder
from random import choice


class Animate:
	
	
	def __init__(self):
		
		# particle dictionary
			self.frames = {
            # magic
            'flame': import_folder('Graphics/particles/flame/frames'),
            'aura': import_folder('Graphics/particles/aura'),
            'heal': import_folder('Graphics/particles/heal/frames'),
            
            # attacks 
            'claw': import_folder('Graphics/particles/claw'),
            'slash': import_folder('Graphics/particles/slash'),
            'sparkle': import_folder('Graphics/particles/sparkle'),
            'leaf_attack': import_folder('Graphics/particles/leaf_attack'),
            'thunder': import_folder('Graphics/particles/thunder'),
 
            # monster deaths
            'squid': import_folder('Graphics/particles/smoke_orange'),
            'raccoon': import_folder('Graphics/particles/raccoon'),
            'spirit': import_folder('Graphics/particles/nova'),
            'bamboo': import_folder("Graphics/particles/bamboo"),
            
            # leafs 
            'leaf': (
                import_folder('Graphics/particles/leaf1'),
                import_folder('Graphics/particles/leaf2'),
                import_folder('Graphics/particles/leaf3'),
                import_folder('Graphics/particles/leaf4'),
                import_folder('Graphics/particles/leaf5'),
                import_folder('Graphics/particles/leaf6'),
                self.reflect_images(import_folder('Graphics/particles/leaf1')),
                self.reflect_images(import_folder('Graphics/particles/leaf2')),
                self.reflect_images(import_folder('Graphics/particles/leaf3')),
                self.reflect_images(import_folder('Graphics/particles/leaf4')),
                self.reflect_images(import_folder('Graphics/particles/leaf5')),
                self.reflect_images(import_folder('Graphics/particles/leaf6'))
                )
            }
	
	def reflect_images(self,frames):
		
		
		new_frames = []
		for frame in frames:
			flipped_frame = pygame.transform.flip(frame,True,True)
	
			new_frames.append(flipped_frame)
			
		return new_frames
	
	def create_grass_particle(self,pos,groups):
			  
			  animation_frames =  choice(self.frames['leaf'])
			  ParticleEffect(pos,animation_frames,groups)
			  
	def create_particle(self,animation_type,pos,groups):
			  animation_frames =  self.frames[animation_type]
			  ParticleEffect(pos,animation_frames,groups)
		
	
			  
			  
			  
	
	
            
     	
class ParticleEffect(pygame.sprite.Sprite):
	
	def __init__(self,pos,animation_frames,groups):
		
		super().__init__(groups)
		
		
		self.sprite_type = "magic"
		self.frame_index = 0
		self.animation_speed = 0.15
		self.frames = animation_frames
		
		self.image = self.frames[self.frame_index]
		
		self.rect = self.image.get_rect(center = pos)
		
	def animate(self):
		self.frame_index += self.animation_speed
		if self.frame_index >= len(self.frames):
			self.kill()
			
		else: self.image = self.frames[int(self.frame_index)]
	
	
	def update(self):
		
		self.animate()
		
	
		