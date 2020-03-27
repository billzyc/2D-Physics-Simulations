import pygame
import math

from particleTile import ParticleTile
import window_info as windowInfo


def drawGameWindow():
  win.fill((255,255,255))
  for i in range(len(particleList)):
    particleList[i].draw(win)


pygame.init()
font = pygame.font.SysFont('arial', 15)
particleList = []
particleBoxSize = 20
for i in range(0, windowInfo.width, particleBoxSize):
  for j in range(windowInfo.ceiling, windowInfo.height, particleBoxSize):
    newParticle = ParticleTile(i, j, particleBoxSize, particleBoxSize)
    particleList.append(newParticle)
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
    for i in range(len(particleList)):
      particleList[i].runInputBox(event)
  drawGameWindow()
  pygame.display.update()
pygame.quit()