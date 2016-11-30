# Chiedu Nduka-Eze 11/22/16 Unit 10
# This program creates a pyramid with 5 rows of different colored bricks
import pygame


class Brick:
   """This class creates a brick that I will later be using for a breakout game"""
   def __init__(self, surface, BrickHeight, BrickWidth, Color):
       self.BrickHeight = BrickHeight
       self.BrickWidth = BrickWidth
       self.Color = Color
       self.surface = surface

   def draw(self, x, y):
       """This function draws a brick where the user specifies. the final o fills in the bricks"""
       pygame.draw.rect(self.surface, self.Color, (x, y, self.BrickWidth, self.BrickHeight), 0)
