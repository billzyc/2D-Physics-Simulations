import pygame
import math

from projectile import Projectile
from grid import Grid
from input_box import InputBox
import window_info as windowInfo

environment = {
  "xResistance": 0,
  "yResistance": - 9.80665
}

def timeToGround( location, velocity, acceleration):
  a = acceleration / 2
  b = velocity
  c = location
  root = math.sqrt(b**2 - 4 * a * c);
  return abs((-b - root) / (2 * a));

def drawGameWindow():
  win.fill((255,255,255))
  for i in range(len(location.y)):
    pygame.draw.rect(win, (0, 0, 0), (location.x[i], location.y[i] + projectile.width / 2, 1, 1))
  instructions = font.render("click anywhere to reset projectile", 1, (0,0,0))
  win.blit(instructions, (200, windowInfo.inputHeight + 20))
  pygame.draw.line(win, (0,0,0), (0, windowInfo.inputHeight),(windowInfo.width,windowInfo.inputHeight))
  pygame.draw.line(win, (0,0,0), (0, windowInfo.groundHeight),(windowInfo.width,windowInfo.groundHeight))
  pygame.draw.rect(win, (0, 0, 0), (location.getCurrentX(), location.getCurrentY(), projectile.width, projectile.width))
  velocityInput.draw(win)
  angleInput.draw(win)
  pygame.display.update()



pygame.init()
font = pygame.font.SysFont('arial', 15)

#enviroment setup
velocityInput = InputBox(50, 50, 50, 25, 'enter the velocity of the initial projectile in m/s:', 20, (220,220,220))
angleInput = InputBox(windowInfo.width/2, 50, 50, 25, 'enter the degree of the initial projectile in degrees above the horizon: ', 20, (220,220,220))
projectile = Projectile(5)
location = Grid()
accumulatedTime = 0
# getProjectileCondition = input("add initial velocity and initial degree? Input y for yes, any key for no: ")
# if(getProjectileCondition == 'y'):
#   projectile.getProjectileConditions()
win = pygame.display.set_mode((windowInfo.width, windowInfo.height))
pygame.display.set_caption("kinematics simulation")

#main lopp
run = True
while run:

  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1]> windowInfo.inputHeight:
      accumulatedTime = pygame.time.get_ticks()
      location.resetX(pygame.mouse.get_pos()[0])
      location.resetY(pygame.mouse.get_pos()[1])
    velocityInput.runInputBox(event)
    angleInput.runInputBox(event)
  
  if(location.getCurrentY() < windowInfo.groundHeight - projectile.width):
    location.calculateLocation(projectile, (pygame.time.get_ticks() - accumulatedTime)/1000, environment)
  
  if(velocityInput.isValueConfirmed):
    try:
      projectile.setVelocity(int(velocityInput.content))
    except:
      print("please enter an integer")
  
  if(angleInput.isValueConfirmed):
    try:
      projectile.setAngle(int(angleInput.content))
    except:
      print("please enter an integer")
  drawGameWindow()
pygame.quit()