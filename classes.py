""" Game class for Mac Gyver Labyrinthe """

import pygame
from pygame.locals import *
from constantes import *

class Level:
	""" Class make a level """
	def __init__ (self, file):
		self.file = file
		self.structure = 0


	def generate(self):
		# Method for generate level with a file
		# Create a general list, contains a liste per toggle lign
		# Open the file
		with open(self.file, "r") as file:
			structure_level = []
			# Browse file lign
			for lign in file:
				lign_level = []
				# Browse sprites (letters) contains in file
				for sprite in lign:
					# Ignore the "\n" of lign end
					if sprite != '\n':
						# Add the sprite at the lign list
						lign_level.append(sprite)
				# Add the ligne at the level list
				structure_level.append(lign_level)
			# Save the structure
			self.structure = structure_level

	def toggle(self, window):
		# Method for toggle the level of the structure send by generate()
		# Load pictures
		#laucher = pygame.image.load(img_launcher).convert()
		#rocket = pygame.image.load(img_rocket).convert()
		#swiss_knife = pygame.image.load(img_knife).convert()
		wall = pygame.image.load("pictures/wall.png").convert_alpha()
		start = pygame.image.load("pictures/start.png").convert_alpha()
		end = pygame.image.load("pictures/end.png").convert_alpha()

		# Browse level list
		num_lign = 0
		for lign in self.structure:
			# Browse lign listes
			num_case = 0
			for sprite in lign:
				# Calcul real position in pixels
				x = num_case * size_sprite
				y = num_case * size_sprite
				if sprite == 'm':	# m = wall
					window.blit(wall, (x,y))
				elif sprite == 'd':	# d = start
					window.blit(start, (x,y))
				elif sprite == 'a':	# a = end
					window.blit(end, (x,y))
				num_case += 1
			num_lign += 1

class Character:
	""" Class make a character """
	def __init__(self, movement, level):
		#Sprites du personnage
		self.movement = pygame.image.load(movement).convert_alpha()
		# Character pixel & cases position 
		self.case_x = 5
		self.case_y = 0
		self.x = 128
		self.y = 0
		# Default move
		self.direction = self.movement
		# Level where the character in
		self.level = self.movement

	def move(self, direction):
		""" Move Method Character """

		# Move to right
		if direction == 'right':
			# Don't get out of the screen
			if self.case_x < 0:
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y][self.case_x+1] != 'm':
					#Move one case
					self.case_x += 1
					# Calcul real pixel position
					self.x = self.case_x * size_sprite

		# Move to left
		if direction == 'left':
			# Don't get out of the screen
			if self.case_x > 0:
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					#Move one case
					self.case_x -= 1
					# Calcul real pixel position
					self.x = self.case_x * size_sprite

		# Move to right
		if direction == 'top':
			# Don't get out of the screen
			if self.case_y > 0:
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					#Move one case
					self.case_y -= 1
					# Calcul real pixel position
					self.y = self.case_y * size_sprite

		# Move to right
		if direction == 'down':
			# Don't get out of the screen
			if self.case_y > 0:
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					#Move one case
					self.case_y += 1
					# Calcul real pixel position
					self.y = self.case_y * size_sprite
