""" Game class for Mac Gyver Labyrinthe """

import pygame
from pygame.locals import *

from constants import *
import random


class Level:
    """ Class make a level """
    def __init__ (self, file):
        self.file = file # lvl.txt
        self.structure = 0

    def generate(self):
        """Method for generate level with a file"""
        # Open the file
        with open(self.file, "r") as file:
            structure_level = [] # Initialized as empty list to save level structure
            # Browse file lign
            for line in file:
                line_level = []
                # Browse sprites (letters) con"tains in file
                for sprite in line:
                    # Ignore the "\n" of lign end
                    if sprite != '\n':
                        # Add the sprite at the lign list
                        line_level.append(sprite)
                # Add the ligne at the level list
                structure_level.append(line_level)
            # Save the structure
            self.structure = structure_level


    def toggle(self, window):
        """Method for toggle the level of the structure send by generate()"""
        # Load pictures
        guard = pygame.image.load(img_guard).convert_alpha()
        wall = pygame.image.load(img_wall).convert_alpha()

        # Browse level list
        num_lign = 0
        for lign in self.structure:
            # Browse lign list
            num_case = 0
            for sprite in lign:
                # Calcul real position in pixels
                x = num_case * size_sprite
                y = num_case * size_sprite
                if sprite == 'w':	# w = wall
                    window.blit(wall, (x,y))
                if sprite == 'e':
                	window.blit(guard, (x,y))
                num_case += 1
            num_lign += 1


class MacGyver:
    """Class make a character"""
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
        # Direction par default
        self.direction = self.right
        # Level where the character in
        self.level = level
        self.item = 0 # Mac gyver have 0 items


    def move(self, direction):
        """Move Method Character"""

        # Move to right
        if direction == 'right':
            # Don't get out of the screen
            if self.case_x < (number_sprite_width - 1):
                # Check if the destination case is not a wall
                if self.level.structure[self.case_y][self.case_x+1] != 'w':
                    # Move one case
                    self.case_x += 1
                    # Calcul real pixel position
                    self.x = self.case_x * size_sprite
            # Check image in good direction
            self.direction = self.right

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'w':
                    self.case_x -= 1
                    self.x = self.case_x * size_sprite
            self.direction = self.left

        if direction == 'top':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'w':
                    self.case_y -= 1
                    self.y = self.case_y * size_sprite
            self.direction = self.top

        if direction == 'down':
            if self.case_y < (number_sprite_height - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'w':
                    self.case_y += 1
                    self.y = self.case_y * size_sprite
            self.direction = self.down


    def take_item(self, *item):
        self.item += 1

    def damage(self):
        self.health -= 1

    def inventory(self):
        text = "Inventory : " + str(self.item)
        return text


class Guardian:
    """Class make a character"""
    def __init__(self, level):
        # Level where the character in 
        self.level = level
        self.health = 1

    def damage(self):
        self.health -= 1

class Item:
    """ Class to create an item """
    def __init__(self, name,  path, level):
        # Initial settings for the item
        self.id = name
        self.health = 1
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * size_sprite
        self.y = self.case_y * size_sprite
        self.sprite = pygame.image.load(path).convert_alpha()

    def randpos(self):
        # Method to place randomly the 'Items' on the map
        while True:
            self.case_x = random.randrange(1, 25)
            self.case_y = random.randrange(1, 14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = self.id
                break
        return self.case_x, self.case_y

    def damage(self):
        self.health -= 1
        self.level.structure[self.case_y][self.case_x] = '0'

    def display(self, window):
        # Display the item on screen
        if self.health > 0:
            window.blit(self.sprite, (self.x, self.y)) 