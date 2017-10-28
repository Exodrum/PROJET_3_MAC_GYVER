#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Mac Gyver Game
Game where you have to pick up objects for win the Gardin.

Script Python
Files : mglabyrinthe.py, classes.py, constantes.py, lvl1 + pictures
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

window = pygame.display.set_mode((size_window_2, size_window))

# Icone
icone = pygame.image.load("img/mac_gyver_right.png")
pygame.display.set_icon(icone)

# Title
pygame.display.set_caption("mglabyrinthe")

# PRINCIPAL LOOP
continu = 1
while continu:
	#Load & toggle home
	home = pygame.image.load(img_home)
	window.blit(home, (0,0))

	#Refresh
	pygame.display.flip()

	#Get variable at 1 for each loop
	continu_game = 1
	continu_home = 1

	# LOOP HOME
	while continu_home:

		# Speed limit of loop
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# If user exit, get variable
			# of loop at 0 for not browse other and shut it.shut
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continu_home = 0
				continu_game = 0
				continu = 0
				# Level choice variable
				choice = 0

			elif event.type == KEYDOWN:
				#Go in game
				if event.key == K_SPACE:
					continu_home = 0 # User exit home
					choice = 'lvl' # Define level loading


	# Check if user make a choice
	# for no load if he exit
	if choice != 0:
		# Loading background
		background = pygame.image.load(img_background).convert()

		# Generate a level become a file
		level = Level(choice)
		level.generate()
		level.toggle(window)

		# Create Mac Gyver
		mg = Character("img/mac_gyver_right.png", "img/mac_gyver_left.png",
		"img/mac_gyver_top.png", "img/mac_gyver_down.png", level)


	# GAME LOOP
	while continu_game:

		# Speed limit loop
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			# If users exit, get variable for carry the game
			# & general variable = 0 for shut the window
			if event.type == QUIT:
				continu_game = 0
				continu = 0

			elif event.type == KEYDOWN:
				# If user press Escap ir, back to home
				if event.key == K_ESCAPE:
					continu_game = 0

				# Key move Mac Gyver
				elif event.key == K_RIGHT:
					mg.move('right')
				elif event.key == K_LEFT:
					mg.move('left')
				elif event.key == K_UP:
					mg.move('top')
				elif event.key == K_DOWN:
					mg.move('down')

				# If mac gyver win 
				"""if mg.status == win:
					print(config["end_msg_win"])
				# If mac gyver lost
				elif mg.status == lost:
					print(config["end_msg_win"])

				# If mac gyver 
				if mg.status != try_again:
					print("Try again ? Press (y/n)")
					continu_game = 0

			else:
				if event.key == K_y:
					mg.reset()
					level.reset()
					end_game = 0
				elif event.key == K_n:
					continu_game = 0"""



		# Toggle new positions
		window.blit(background, (0,0))
		level.toggle(window)
		window.blit(mg.direction, (mg.x, mg.y)) #mg.direction = l'image dans la bonne direction
		pygame.display.flip()

		