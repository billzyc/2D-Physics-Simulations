import pygame
import math

from particle import Particle
import window_info as windowInfo
from pygame_util_library import TextBox


def drawGameWindow():
  win.fill((255,255,255))
  drawGrid()
  for i in range(len(particleList)):
    particleList[i].draw(win)

def drawGrid():
  gridGapLength = 50
  orginX = windowInfo.width/2
  orginY = int((windowInfo.height - windowInfo.ceiling)/2)
  #y-axis
  pygame.draw.line(win, (0,0,155), (orginX, windowInfo.height),(orginX, windowInfo.ceiling))
  for i in range( 0, windowInfo.width, gridGapLength):
    xLabel = TextBox(i, orginY, 5, 5, f'{str(int(orginX - i) * -1)} cm', 5)
    xLabel.draw(win)
  #x-axis
  pygame.draw.line(win, (0,0,155), (0, round(windowInfo.height - windowInfo.ceiling)/2),(windowInfo.width,round(windowInfo.height - windowInfo.ceiling)/2))

  for i in range( windowInfo.ceiling, windowInfo.height, gridGapLength):
    xLabel = TextBox(orginX, i, 5, 5, f'{str(orginY - i)} cm', 5)
    xLabel.draw(win)

pygame.init()
font = pygame.font.SysFont('arial', 15)
particleList = []
#enviroment setup
win = pygame.display.set_mode((windowInfo.width, windowInfo.height))
pygame.display.set_caption("electrostatics simulation")

#main loop
run = True
particleSetupInProgress = (False, False)
targetParticle = [None, False] # [Instance of particle,  has the force been calculated]
while run:
  if(particleSetupInProgress[0] and particleSetupInProgress[1].getIsChargeAdded()):
    particleSetupInProgress = (False, False)
  if(targetParticle[0] and not targetParticle[1]):
    targetParticle[0].calculateTotalForce(particleList)
    targetParticle[1] = True
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN and not particleSetupInProgress[0]:
      position = pygame.mouse.get_pos()
      isParticleClicked = False
      for i in range(len(particleList)):
        if particleList[i].checkClicked(position):
          particleList[i].isTarget = True
          targetParticle = [particleList[i], False]
          isParticleClicked = True
        else:
          particleList[i].isTarget = False
      if not isParticleClicked:
        newParticle = Particle(position[0], position[1], 8)
        particleList.append(newParticle)
        particleSetupInProgress = (True, newParticle)
    for i in range(len(particleList)):
      particleList[i].runParticle(event)
  drawGameWindow()
  pygame.display.update()
pygame.quit()