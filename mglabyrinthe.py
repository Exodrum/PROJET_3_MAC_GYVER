#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Mac Gyver Game
Game where you have to pick up objects for win the Gardin.

Script Python
Files : mglabyrinthe.py, classes.py, constantes.py, n1, n2 + pictures
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

window = pygame.display.set_mode((size_window_2, size_window))

# Icone
icone = pygame.image.load("pictures/mac_gyver.png")
pygame.display.set_icon(icone)

# Title
pygame.display.set_caption("mglabyrinthe")

# PRINCIPAL LOOP
carry = 1
while carry:
	#Load & toggle home
	home = pygame.image.load("pictures/home.jpg")
	window.blit(home, (0,0))

	#Refresh
	pygame.display.flip()

	#Get variable at 1 for each loop
	carry_game = 1
	carry_home = 1

	# LOOP HOME
	while carry_home:

		# Speed limit of loop
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# If user exit, get variable
			# of loop at 0 for not browse other and shut it.shut
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				carry_home = 0
				carry_game = 0
				carry = 0
				# Level choice variable
				choice = 0

			elif event.type == KEYDOWN:
				#Go in game
				if event.key == K_SPACE:
					carry_home = 0 # User exit home
					choice = 'n1' # Define level loading


	# Check if user make a choice
	# for no load if he exit
	if choice != 0:
		# Loading background
		background = pygame.image.load("pictures/background.png").convert()

		# Generate a level become a file
		level = Level(choice)
		level.generate()
		level.toggle(window)

		# Create Mac Gyver
		mg = Character("pictures/mac_gyver.png", level)


	# GAME LOOP
	while carry_game:

		# Speed limit loop
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# If users exit, get variable for carry the game
			# & general variable = 0 for shut the window
			if event.type == QUIT:
				carry_game = 0
				carry = 0

			elif event.type == KEYDOWN:
				# If user press Escap ir, back to home
				if event.key == K_ESCAPE:
					carry_game = 0

				# Key move Mac Gyver
				elif event.key == K_RIGHT:
					mg.move('right')
				elif event.key == K_LEFT:
					mg.move('left')
				elif event.key == K_UP:
					mg.move('up')
				elif event.key == K_DOWN:
					mg.move('down')		

		# Toggle new positions
		window.blit(background, (0,0))
		level.toggle(window)
		window.blit(mg.direction, (mg.x, mg.y)) #mg.direction = l'image dans la bonne direction
		pygame.display.flip()

		#Victory -> Back to home
		#if level.structure[mg.case_y][mg.case_x] == 'a':
			#continuer_jeu = 0