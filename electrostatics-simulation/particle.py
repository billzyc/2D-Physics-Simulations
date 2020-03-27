import pygame
from pygame_util_library import InputBox
import math

class Particle:
  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.isTarget = False
    self.charge = False
    self.input = InputBox(x, y + round(radius * 4), 50, 20, 'enter charge in microcoulombs', 5, (100, 100, 100), (212,235, 242))
    self.totalForce = 0

  def isChargeAdded(self):
    return self.input.isValueConfirmed

  def draw(self, window):
    if (self.isTarget):
      pygame.draw.circle(window, (0,0,255), (self.x + self.radius, self.y + self.radius), self.radius)
    else:
      pygame.draw.circle(window, (0,0,0), (self.x + self.radius, self.y + self.radius), self.radius)
    if not self.isChargeAdded():
      self.input.draw(window)
    else:
      self.charge = int(self.input.content) * 1e-6
    if(self.charge):
      fontsize = 15
      font = pygame.font.SysFont('arial', fontsize)
      content = font.render(str(self.charge / 1e-6), 1, (255,255,255))
      window.blit(content, (self.x + round((self.radius + fontsize) * 0.4) , self.y + round((self.radius + fontsize) * 0.4)))
    if(self.isTarget):
      fontsize = 20
      font = pygame.font.SysFont('arial', fontsize)
      content = font.render(f'total electric force is {self.totalForce}', 1, (0,0,0))
      window.blit(content, (self.x , self.y + self.radius * 4))

  def runParticle(self, event):
    if not self.isChargeAdded():
      self.input.runInputBox(event)

  def checkClicked(self, clickedPos):
    if clickedPos[0] > self.x and clickedPos[0] < self.x + self.radius * 2 and clickedPos[1] > self.y and clickedPos[1] < self.y + self.radius * 2:
        return True
    else:
      return False

  def getIsChargeAdded(self):
    return self.isChargeAdded()

  def addForce(self, force):
    self.totalForce = self.totalForce + force

  def calculateDistance( self, secondCharge):
    xDifference = self.x - secondCharge.x
    yDifference = self.y - secondCharge.y
    return math.sqrt(xDifference**2 + yDifference**2)

  def coulombsLaw(self, secondCharge):
    eNaught = 8.854e-12
    coulombConstant = 1 / (4 * math.pi * eNaught);
    distance = self.calculateDistance(secondCharge)
    return coulombConstant * (self.charge * secondCharge.charge / distance**2);

  def calculateTotalForce(self, charges):
    for i in range(len(charges)):
        if(charges[i] != self):
            force = self.coulombsLaw(charges[i]);
            self.addForce(force);

    return self.totalForce;