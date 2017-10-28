""" Game class for Mac Gyver Labyrinthe """

import pygame
from pygame.locals import *
from constantes import *
#from random import randint


class Level:
	""" Class make a level """
	def __init__ (self, file):
		self.file = file
		self.structure = 0

	"""def reset(self):
		# Methode generate random position for items after game reset
		# Browse item file
		for item in self.items:
			# Give a position to item on empty position 0 (no wall, no character)
			self.file[self.items[item].pos_y][self.items[item].pos_x] = "0"
			self.items[item] = Item(self.random_position())"""


	def generate(self):
		# Method for generate level with a file
		# Create a general list, contains a list per toggle lign
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
		wall = pygame.image.load(img_wall).convert_alpha()
		start = pygame.image.load(img_start).convert_alpha()
		end = pygame.image.load(img_end).convert_alpha()

		# Browse level list
		num_lign = 0
		for lign in self.structure:
			# Browse lign list
			num_case = 0
			for sprite in lign:
				# Calcul real position in pixels
				x = num_case * size_sprite
				y = num_case * size_sprite
				if sprite == 'w':	# m = wall
					window.blit(wall, (x,y))
				elif sprite == 's':	# d = start
					window.blit(start, (x,y))
				elif sprite == 'e':	# e = end
					window.blit(end, (x,y))
				num_case += 1
			num_lign += 1


"""class Item:
	# Describe an item
	def __init__(self, position):

		self.launcher = pygame.image.load(img_launcher).convert_alpha()
		self.rocket = pygame.image.load(img_rocket).convert_alpha()

		self.case_x = position[0]
		self.case_y = position[1]
		self.show = 1

	@property
	def pixel_position(self):
		#Pixel position of the item
		return [self.case_x * sprite_size, self.case_y * sprite_size]"""


class Character:
	""" Class make a character """
	def __init__(self, right, left, top, down, level):
		#Sprites du personnage
		self.right = pygame.image.load(right).convert_alpha()
		self.left = pygame.image.load(left).convert_alpha()
		self.top = pygame.image.load(top).convert_alpha()
		self.down = pygame.image.load(down).convert_alpha()
		# Character pixel & cases position 
		self.case_x = 4
		self.case_y = 0
		self.x = 128
		self.y = 0
		# Default direction
		self.direction = self.right
		# Level where the character in
		self.level = level


	"""def reset(self):
		# Give an character initial position and clear his items
		self.case_y, self.case_x = self.initial_position(self.level)
		self.num_items = 0"""


	def move(self, direction):
		""" Move Method Character """

		# Move to right
		if direction == 'right':
			# Don't get out of the screen
			if self.case_x < (number_sprite_width - 1):
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y][self.case_x+1] != 'w':
					#Move one case
					self.case_x += 1
					# Calcul real pixel position
					self.x = self.case_x * size_sprite

		# Move to left
		if direction == 'left':
			# Don't get out of the screen
			if self.case_x > 0:
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y][self.case_x-1] != 'w':
					#Move one case
					self.case_x -= 1
					# Calcul real pixel position
					self.x = self.case_x * size_sprite

		# Move to right
		if direction == 'top':
			# Don't get out of the screen
			if self.case_y > 0:
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y-1][self.case_x] != 'w':
					#Move one case
					self.case_y -= 1
					# Calcul real pixel position
					self.y = self.case_y * size_sprite

		# Move to right
		if direction == 'down':
			# Don't get out of the screen
			if self.case_y < (number_sprite_height - 1):
				# Check if the destination case is not a wall
				if self.level.structure[self.case_y+1][self.case_x] != 'w':
					#Move one case
					self.case_y += 1
					# Calcul real pixel position
					self.y = self.case_y * size_sprite

