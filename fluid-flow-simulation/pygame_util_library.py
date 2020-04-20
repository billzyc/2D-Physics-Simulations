import pygame


class InputBox:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        promptText="",
        defaultValue="",
        fontSize=20,
        bgColor=(255, 255, 255),
        activeColor=(68, 85, 90),
        textColor=(0, 0, 0),
    ):
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
        self.content = defaultValue
        self.font = pygame.font.SysFont("arial", 15)
        self.isValueConfirmed = False

    def draw(self, window):
        if self.isActive == True:
            self.image.fill(self.activeColor)
        else:
            self.image.fill(self.bgColor)
        content = self.font.render(self.content, 1, self.textColor)
        window.blit(self.image, (self.x, self.y))
        if self.promptText:
            instructions = self.font.render(self.promptText, 1, self.textColor)
            window.blit(
                instructions, (self.x, self.y - round(self.y / 50) - self.fontSize)
            )
        window.blit(
            content,
            (
                self.x + round(self.width / 10),
                self.y + round(self.height / 2) - round(self.fontSize / 2),
            ),
        )

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
        elif self.isActive and self.content:
            self.isActive = False
            self.isValueConfirmed = True

    def updateContent(self, key):
        delete = 8
        if key == delete or key == pygame.K_DELETE or key == pygame.K_BACKSPACE:
            if len(self.content) > 0:
                self.content = self.content[0:-1]

        elif key == pygame.K_RETURN:
            self.isActive = False
            self.isValueConfirmed = True

        else:
            self.content += chr(key)


class TextBox:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        content,
        fontSize=20,
        bgColor=False,
        textColor=(0, 0, 0),
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.fontSize = fontSize
        self.bgColor = bgColor
        self.textColor = textColor
        self.content = pygame.font.SysFont("arial", 15).render(
            content, 1, self.textColor
        )

    def draw(self, window):
        if self.bgColor:
            self.image.fill(self.bgColor)
            window.blit(self.image, (self.x, self.y))
        window.blit(self.content, (self.x, self.y))


def drawPixel(window, x, y, color=(255, 0, 0)):
    pygame.draw.rect(window, color, (x, y, 1, 1))


class ClickButton:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        promptText="",
        fontSize=20,
        bgColor=(255, 255, 255),
        textColor=(0, 0, 0),
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.fontSize = fontSize
        self.bgColor = bgColor
        self.textColor = textColor
        self.promptText = promptText
        self.font = pygame.font.SysFont("arial", 15)

    def draw(self, window):
        self.image.fill(self.bgColor)
        window.blit(self.image, (self.x, self.y))
        if self.promptText:
            instructions = self.font.render(self.promptText, 1, self.textColor)
            window.blit(
                instructions, (self.x, self.y - round(self.y / 50) - self.fontSize)
            )

    def runInputBox(self, event, action):
        if event.type == pygame.MOUSEBUTTONDOWN and self.checkClicked(
            pygame.mouse.get_pos()
        ):
            action()

    def checkClicked(self, clickedPos):
        if clickedPos[0] > self.x and clickedPos[0] < self.x + self.width:
            if clickedPos[1] > self.y and clickedPos[1] < self.y + self.height:
                return True
        return False
