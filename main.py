#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Mac Gyver Game
Game where you have to pick up items for win the Gard.

Script Python
Files : mglabyrinthe.py, classes.py, constantes.py, lvl1 + pictures
"""

import pygame    # import module pygame
from pygame.locals import *    # import all lib pygame

from classe import *    # import all class from a file
from constants import *    # import all constants from a file

pygame.init()
window = pygame.display.set_mode((size_window_2, size_window))
# Icone
icone = pygame.image.load(img_icone)
pygame.display.set_icon(icone)
# Title
pygame.display.set_caption(window_title)
# Font
myfont = pygame.font.SysFont('Arial', 20, True)

# PRINCIPAL LOOP
continu = 1
while continu:
    #Load & toggle home
    home = pygame.image.load(img_home).convert()
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
            if event.type == QUIT or event.type == KEYDOWN and\
             event.key == K_ESCAPE:
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
        mac_gyver = MacGyver("img/mac_gyver_right.png",
            "img/mac_gyver_left.png",
            "img/mac_gyver_top.png", 
            "img/mac_gyver_down.png", 
            level)

        # Create Guardian
        guard = Guardian(level)

        # Create Items
        launcher = Item("n", img_launcher, level)
        rocket = Item("r", img_rocket, level)

    # GAME LOOP
    while continu_game:
        # Create inventory interface
        inventory = myfont.render(mac_gyver.inventory(), False, (255, 255, 255))
        # Speed limit loop
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If users exit, get variable for carry the game
            # and general variable = 0 for shut the window
            if event.type == QUIT:
                continu_game = 0
                continu = 0

            elif event.type == KEYDOWN:
                # If user press Escap ir, back to home
                if event.key == K_ESCAPE:
                    continu_game = 0

                # Key move Mac Gyver
                elif event.key == K_RIGHT:
                    mac_gyver.move('right')
                elif event.key == K_LEFT:
                    mac_gyver.move('left')
                elif event.key == K_UP:
                    mac_gyver.move('top')
                elif event.key == K_DOWN:
                    mac_gyver.move('down')

        pygame.display.flip()

        """ Methode take an item """
        if level.structure[mac_gyver.case_y][mac_gyver.case_x] == launcher.id:
            launcher.damage()
            mac_gyver.take_item()
        if level.structure[mac_gyver.case_y][mac_gyver.case_x] == rocket.id:
            rocket.damage()
            mac_gyver.take_item()

        """ Guard interaction """
        if level.structure[mac_gyver.case_y][mac_gyver.case_x] == 'l':
            if mac_gyver.item >= 2:
                guard.damage()
                level.structure[mac_gyver.case_y][mac_gyver.case_x] = '0'


            # LOOSE
            else:
                loose = 1
                while loose:
                    pygame.time.Clock().tick(30)
                    loose = pygame.image.load("img/loose.png")
                    window.blit(loose, pos_loose)
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and\
                         event.key == K_ESCAPE:
                            loose = 0
                            continu_game = 0
                    pygame.display.flip()

        # WIN
        if level.structure[mac_gyver.case_y][mac_gyver.case_x] == 'e' and mac_gyver.item >= 2:
            win = 1
            while win:
                pygame.time.Clock().tick(30)
                win = pygame.image.load("img/win.png")
                window.blit(win, pos_win)
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key == K_ESCAPE:
                        win = 0
                        continu_game = 0
                pygame.display.flip()
		

        # Toggle new positions
        window.blit(background, (0,0))
        window.blit(inventory, pos_inventory)
        level.toggle(window)
        launcher.display(window)
        rocket.display(window)
        window.blit(mac_gyver.direction, (mac_gyver.x, mac_gyver.y)) #dk.direction = l'image dans la bonne direction
        pygame.display.flip()
