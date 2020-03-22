import math

class Ball:
  def __init__(self, width):
    self.velocityX = 0
    self.velocityY = 0
    self.velocity = 0
    self.initialVelocityX = 0
    self.initialVelocityY = 0
    self.initialVelocity = 0
    self.angle = 0
    self.width = width
  
  def getBallConditions(self):
    initialVelocity = int(input("enter the velocity of the initial ball in m/s: "))
    initialAngle = int(input("enter the degree of the initial ball in degrees above the horizon: "))
    self.angle = initialAngle
    self.initialVelocity = initialVelocity
    self.initialVelocityX = math.cos(self.angle * math.pi / 180) * self.initialVelocity;
    self.initialVelocityY = math.sin(self.angle * math.pi / 180) * self.initialVelocity;
    self.velocityX = self.initialVelocityX
    self.velocityY = self.initialVelocityY

  def velocityKinematicFormula(self, initialVelocity, time, acceleration):
    return initialVelocity + acceleration * time

  def calculateCurrentVelocity(self, time, resistanceX, resistanceY):
    self.velocityX = self.velocityKinematicFormula(self.initialVelocityX, time, resistanceX);
    self.velocityY = self.velocityKinematicFormula(self.initialVelocityY, time, resistanceY);
    self.velocity = math.sqrt(self.velocityX**2 + self.velocityY**2);
    # print(f"current velocity: {self.velocity} m/s")
  

