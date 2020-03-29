import pygame
import math

from particle import Particle
import window_info as windowInfo
from pygame_util_library import TextBox


def drawGameWindow():
  win.fill((255,255,255))

def drawGrid():
  pass

pygame.init()
font = pygame.font.SysFont('arial', 30)
#enviroment setup
win = pygame.display.set_mode((windowInfo.width, windowInfo.height))
pygame.display.set_caption("fluid flow simulation")
#main loop
run = True
while run:
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  drawGameWindow()
  pygame.display.update()
pygame.quit()