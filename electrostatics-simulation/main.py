import pygame
import math

from particle import Particle
import window_info as windowInfo


def drawGameWindow():
  win.fill((255,255,255))
  for i in range(len(particleList)):
    particleList[i].draw(win)

# def isParticleClicked(position):
#   isParticleClicked = False
#   for i in range(len(particleList)):
#     if particleList[i].checkClicked(position):
#       particleList[i].isTarget = True
#       targetParticle = particleList[i]
#       isParticleClicked = True
#     else:
#       particleList[i].isTarget = False
#   return isParticleClicked

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
        newParticle = Particle(position[0], position[1], 12)
        particleList.append(newParticle)
        particleSetupInProgress = (True, newParticle)
    for i in range(len(particleList)):
      particleList[i].runParticle(event)
  drawGameWindow()
  pygame.display.update()
pygame.quit()