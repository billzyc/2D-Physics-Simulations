import pygame
import math

from projectile import Projectile
from grid import Grid
from pygame-util-library import InputBox
import window_info as windowInfo


def drawGameWindow():
  win.fill((255,255,255))
  pygame.display.update()



pygame.init()
font = pygame.font.SysFont('arial', 15)

#enviroment setup
win = pygame.display.set_mode((windowInfo.width, windowInfo.height))
pygame.display.set_caption("kinematics simulation")

#main lopp
run = True
while run:

  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  drawGameWindow()
pygame.quit()