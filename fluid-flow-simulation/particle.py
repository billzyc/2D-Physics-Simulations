import numpy as np


class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.prevPos = np.array([0, 0])
        self.velocity = np.array([0, 0])
        self.force = np.array([0, 0])
        self.acceleration = np.array([0, 0])
        self.rho = 0
        self.rhoNear = 0
        self.pressure = 0
        self.mass = 1
        self.pressureNear = 0
        self.sigma = 100
        self.beta = 50
        self.neighbors = []

    def calculateAcceleration(self):
        self.acceleration = self.force / self.mass

    def calculateAverageVelocity(self, time):
        self.velocity = (self.pos - self.prevPos) / time

    def positionKinematicFormula(self, time):
        return (self.velocity * time) + (self.acceleration * time ** 2 / 2)

    def calculateLocation(self, secondsPassed):
        self.calculateAcceleration()
        self.pos = self.pos + self.positionKinematicFormula(secondsPassed)
        self.calculateAverageVelocity(secondsPassed)
