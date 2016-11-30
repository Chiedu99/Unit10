# Chiedu Nduka-Eze 11/22/16 Unit 10
# This program creates a pyramid with 5 rows of different colored bricks
import pygame, sys
from pygame.locals import *
import brick


pygame.init()
mainSurface = pygame.display.set_mode((500, 400), 0, 32)


BLUE = (0, 0, 255)


RED = (255, 0, 0)


BLACK = (0, 0, 0)


GREEN = (0, 255, 0)


GOLDROD = (184, 131, 11)


WHITE = (255, 255, 255)


mainSurface.fill(WHITE)


listColors = [BLACK, GREEN, GOLDROD, BLUE, RED]


SPACES = 5


height = mainSurface.get_height()


numberOfBricks = 9


widthOfBrick = (mainSurface.get_width() - ((numberOfBricks + 1) * SPACES ))/ 9


xPos = SPACES


yPos = height - 25


rowNumber = 0
# This loop creates a brick, places them, and changes the color for all 5 rows
for color in listColors:
   # This indents the first brick of each row
   xPos = rowNumber * (widthOfBrick + SPACES)
   for x in range(numberOfBricks):
       pie = brick.Brick(mainSurface, 25, widthOfBrick, color)
       pie.draw(xPos, yPos)
       xPos += (widthOfBrick + SPACES)

   yPos -= 30
   xPos = SPACES
   numberOfBricks -= 2
   rowNumber += 1


pygame.display.update()
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
