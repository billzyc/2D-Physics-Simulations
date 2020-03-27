import pygame

class ParticleTile:
  def __init__(self, x, y ,width, height, promptText='', fontSize = 20, bgColor = (100,100,100), activeColor = (68,85,90), textColor = (0,0,0)):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.image = pygame.Surface((width, height))
    self.fontSize = fontSize
    self.bgColor = bgColor
    self.textColor = textColor
    self.activeColor = activeColor
    self.isActive = False
    self.promptText = promptText
    self.charge = ""
    self.font = pygame.font.SysFont('arial', 15)
    self.isValueConfirmed = False

  def draw(self, window):
    if self.isActive == True:
      self.image.fill(self.activeColor)
    else:
      self.image.fill(self.bgColor)
    content = self.font.render(self.charge, 1, self.textColor)
    window.blit(self.image, (self.x, self.y))
    if self.isValueConfirmed == True:
      pygame.draw.circle(window, (0,0,255), (self.x + round(self.width/2), self.y + round(self.width/2)), round(self.width/2))
    # if self.promptText:
    #   instructions = self.font.render(self.promptText, 1, self.textColor)
    #   window.blit(instructions, (self.x  + round(self.width/2) , self.y + round(self.width/2) - self.fontSize))
    window.blit(content, (self.x + round(self.width/4), self.y + round(self.width/4)))

  def runInputBox(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.checkClicked(pygame.mouse.get_pos())

    if event.type == pygame.KEYDOWN:
      if self.isActive:
        self.updateContent(event.key)

  def checkClicked(self, clickedPos):
    if clickedPos[0] > self.x and clickedPos[0] < self.x + self.width:
      if clickedPos[1] > self.y and clickedPos[1] < self.y + self.height:
        self.isActive = True
    elif self.isActive and self.charge:
      self.isActive = False
      self.isValueConfirmed = True

  def updateContent(self, key):
    delete = 8
    if key == delete or key == pygame.K_DELETE or key == pygame.K_BACKSPACE:
      if len(self.charge) > 0:
        self.charge = self.charge[0:-1]

    elif key ==pygame.K_RETURN:
      self.isActive = False
      self.isValueConfirmed = True

    else:
      self.charge += chr(key)
  
  def getCharge(self):
    return int(self.charge)