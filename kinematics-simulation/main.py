import pygame
import math

from ball import Ball
from grid import Grid
import windowInfo

environment = {
  "xResistance": 0,
  "yResistance": -9.81
}

def timeToGround( location, velocity, acceleration):
  a = acceleration / 2
  b = velocity
  c = location
  root = math.sqrt(b**2 - 4 * a * c);
  return abs((-b - root) / (2 * a));

def drawGameWindow():
  instructions = font.render("please enter simulation configuration", 1, (0, 0 , 0))
  win.blit(instructions, (500, 50))
  pygame.draw.line(win, (0,0,0), (0, windowInfo.groundHeight),(windowInfo.width,windowInfo.groundHeight))
  pygame.draw.rect(win, (0, 0, 0), (location.x, location.y, simulatedBall.width, simulatedBall.width))
  pygame.display.update()
  win.fill((255,255,255))


#main lopp
pygame.init()
font = pygame.font.SysFont('arial', 15)
simulatedBall = Ball(5)
location = Grid()
accumulatedTime = 0
getBallCondition = input("add initial velocity and initial degree? Input y for yes, any key for no: ")
if(getBallCondition == 'y'):
  simulatedBall.getBallConditions()
win = pygame.display.set_mode((windowInfo.width, windowInfo.height))
pygame.display.set_caption("kinematics simulation")
run = True
while run:
  if(location.y < windowInfo.groundHeight - simulatedBall.width):
    location.calculateLocation(simulatedBall, (pygame.time.get_ticks() - accumulatedTime)/1000, environment)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      accumulatedTime = pygame.time.get_ticks()
      location.setAllX(pygame.mouse.get_pos()[0])
      location.setAllY(pygame.mouse.get_pos()[1])

  drawGameWindow()
pygame.quit()