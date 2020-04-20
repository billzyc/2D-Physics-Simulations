import pygame
import numpy as np
from math import *
import random
from pygame.locals import *

from simulationEnvironment import SimulationEnvironment
from consts import *
from particle import Particle
from neighbor import Neighbor
import window_info as windowInfo
from pygame_util_library import InputBox, ClickButton


def drawGameWindow():
    win.fill((255, 255, 255))
    kInput.draw(win)
    kNearInput.draw(win)
    gravityInput.draw(win)
    particleSpacingInput.draw(win)
    restartButton.draw(win)
    numOfParticles.draw(win)
    for targetParticle in simulatedEnvironment.particles:
        pygame.draw.circle(
            win,
            (0, 0, 255),
            (
                int(round(targetParticle.pos[0])),
                int(round(windowInfo.height - targetParticle.pos[1])),
            ),
            round(physicalConsts["supportRadius"]),
        )


def runSimulation():
    # event loop
    if kInput.isValueConfirmed:
        try:
            physicalConsts["k"] = float(kInput.content)
        except:
            print("please try another float or int value")
    if kNearInput.isValueConfirmed:
        try:
            physicalConsts["kNear"] = float(kNearInput.content)
        except:
            print("please try another float or int value")
    if gravityInput.isValueConfirmed:
        try:
            physicalConsts["gravitationalConstant"] = float(gravityInput.content)
        except:
            print("please try another float or int value")
    if particleSpacingInput.isValueConfirmed:
        try:
            physicalConsts["particleSpacing"] = float(particleSpacingInput.content)
        except:
            print("please try another float or int value")
    if numOfParticles.isValueConfirmed:
        try:
            physicalConsts["numberOfParticles"] = float(numOfParticles.content)
        except:
            print("please try another float or int value")
    drawGameWindow()
    simulatedEnvironment.updateParticle()
    simulatedEnvironment.particleCalculations()
    pygame.display.update()


def resetSimulation():
    simulatedEnvironment.numberOfParticles = physicalConsts["numberOfParticles"]
    simulatedEnvironment.restartSimulation(windowInfo.width, windowInfo.height)


# environment setup
pygame.init()
simulatedEnvironment = SimulationEnvironment(
    physicalConsts["supportRadius"],
    physicalConsts["gravitationalConstant"],
    physicalConsts["k"],
    physicalConsts["kNear"],
    physicalConsts["restDensity"],
    physicalConsts["maxVel"],
    physicalConsts["maxForce"],
    physicalConsts["velDamp"],
    physicalConsts["forceDamp"],
)
font = pygame.font.SysFont("arial", 30)
win = pygame.display.set_mode((windowInfo.width, windowInfo.height), DOUBLEBUF)
pygame.display.set_caption("fluid flow simulation")

simulatedEnvironment.numberOfParticles = physicalConsts["numberOfParticles"]
simulatedEnvironment.createParticles(windowInfo.width, windowInfo.height)

isProgramActive = True

# Input set up
kInput = InputBox(50, 50, 50, 25, "k:", str(physicalConsts["k"]), 20, (220, 220, 220),)

kNearInput = InputBox(
    150, 50, 50, 25, "kNear:", str(physicalConsts["kNear"]), 20, (220, 220, 220),
)

gravityInput = InputBox(
    50,
    150,
    50,
    25,
    "gravity constant:",
    str(physicalConsts["gravitationalConstant"]),
    20,
    (220, 220, 220),
)

particleSpacingInput = InputBox(
    150,
    150,
    50,
    25,
    "particle spacing",
    str(physicalConsts["particleSpacing"]),
    20,
    (220, 220, 220),
)

numOfParticles = InputBox(
    50,
    250,
    50,
    25,
    "number of particles",
    str(physicalConsts["numberOfParticles"]),
    20,
    (220, 220, 220),
)

restartButton = ClickButton(150, 250, 50, 25, "Click to Restart", 20, (0, 220, 0),)

# main loop
while isProgramActive:
    simulatedEnvironment.previousTime = simulatedEnvironment.currentTime
    simulatedEnvironment.currentTime += 1
    runSimulation()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isProgramActive = False
        restartButton.runInputBox(event, resetSimulation)
        kInput.runInputBox(event)
        kNearInput.runInputBox(event)
        gravityInput.runInputBox(event)
        particleSpacingInput.runInputBox(event)
        numOfParticles.runInputBox(event)
pygame.quit()
