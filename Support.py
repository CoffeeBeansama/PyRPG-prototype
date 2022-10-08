from csv import reader
import pygame
from os import walk
def import_csv_layout(path):
	
	terrain_map = []
	with open(path) as level_map:
		layout = reader(level_map,delimiter = ",")
		for row in layout:
			terrain_map.append(list(row))
		return terrain_map


def import_folder(path):
    surface_list = []
    paths = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            paths.append(full_path)
        
        paths.sort(key = lambda x: x[-6:-4] )
        for element in paths:
            image_surf = pygame.image.load(element).convert_alpha()
            surface_list.append(image_surf)
    
    return surface_list

		
		


		


	
	