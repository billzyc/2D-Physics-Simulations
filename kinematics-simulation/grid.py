import window_info as windowInfo
class Grid:

  def __init__(self):
    self.initialX = 100
    self.initialY = 100
    self.x = [100]
    self.y = [100]

  def resetX(self, x=100):
    self.x = [x]
    self.initialX = x

  def resetY(self, y=100):
    self.y = [y]
    self.initialY = y

  def getCurrentX(self):
    return self.x[-1]

  def getCurrentY(self):
    return self.y[-1]

  def getHeight(self):
    initialHeight = windowInfo.height - int(input("enter the height of the initial ball in meters: "))
    self.initialY = initialHeight
    self.y = [self.initialY]

  def positionKinematicFormula (self, initialVelocity, time, acceleration):
    return ((initialVelocity * time) + (acceleration * time * time / 2))

  def calculateLocation(self, currentBall, secondsPassed, environment):
    x =  self.initialX + self.positionKinematicFormula(currentBall.initialVelocityX, secondsPassed, environment['xResistance'])
    y = self.initialY - self.positionKinematicFormula(currentBall.initialVelocityY, secondsPassed, environment['yResistance'])
    self.x.append(x)
    self.y.append(y)