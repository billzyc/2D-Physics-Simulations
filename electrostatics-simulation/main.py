import pygame
import math

from pygame_util_library import InputBox
import window_info as windowInfo


def drawGameWindow():
  win.fill((255,255,255))
  pygame.display.update()



pygame.init()
font = pygame.font.SysFont('arial', 15)

#enviroment setup
win = pygame.display.set_mode((windowInfo.width, windowInfo.height))
pygame.display.set_caption("electrostatics simulation")

#main loop
run = True
while run:

  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  drawGameWindow()
pygame.quit()