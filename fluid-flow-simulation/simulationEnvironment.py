import numpy as np
from math import *

from particle import Particle
from neighbor import Neighbor


class SimulationEnvironment:
    def __init__(
        self,
        supportRadius,
        g,
        k,
        kNear,
        restDensity,
        maxVel,
        maxForce,
        velDamp,
        forceDamp,
        xMax,
        yMax
    ):
        self.supportRadius = supportRadius
        self.g = g
        self.k = k
        self.kNear = kNear
        self.restDensity = restDensity
        self.maxVel = maxVel
        self.maxForce = maxForce
        self.velDamp = velDamp
        self.forceDamp = forceDamp
        self.restDensity
        self.xMax = xMax
        self.yMax = yMax
        self.particles = []
        self.currentTime = 0
        self.previousTime = 0
        self.numberOfParticles = 100

    def particleCalculations(self):
        for i in range(len(self.particles)):
            # Density calculations
            densityFar = densityNear = 0
            targetParticle = self.particles[i]
            targetParticle.rho = targetParticle.rhoNear = 0
            for j in range(i + 1, len(self.particles)):
                neighborParticle = self.particles[j]
                distanceVector = neighborParticle.pos - targetParticle.pos
                distance = np.linalg.norm(distanceVector)
                if distance ** 2 < self.supportRadius ** 2:
                    weightedDistance = 1 - distance / self.supportRadius
                    densityFar += weightedDistance ** 2
                    densityNear += weightedDistance ** 3
                    neighborParticle.rho += weightedDistance ** 2
                    neighborParticle.rhoNear += weightedDistance ** 3
                    newNeighbor = Neighbor(neighborParticle, weightedDistance)
                    targetParticle.neighbors.append(newNeighbor)
            targetParticle.rho += densityFar
            targetParticle.rhoNear += densityNear

            # Pressure calculations
            targetParticle.press = self.k * (targetParticle.rho - self.restDensity)
            targetParticle.pressNear = self.kNear * targetParticle.rhoNear
            dX = np.array([0, 0])
            for neighborEntry in targetParticle.neighbors:
                neighborParticle = neighborEntry.particle
                distanceVector = neighborParticle.pos - targetParticle.pos
                dm = (
                    targetParticle.pressure + neighborParticle.pressure
                ) * neighborEntry.weightedDistance + (
                    targetParticle.pressNear + neighborParticle.pressureNear
                ) * (
                    neighborEntry.weightedDistance ** 2
                )
                directionOfForce = (
                    distanceVector / np.linalg.norm(distanceVector)
                ) * dm
                dX = dX + directionOfForce
                neighborParticle.force = neighborParticle.force + directionOfForce
            targetParticle.force = targetParticle.force - dX

    def physicalLimiter(self, targetParticle):
        if (
            targetParticle.velocity[0] > self.maxVel
            or targetParticle.velocity[0] < -self.maxVel
        ):
            targetParticle.velocity[0] = targetParticle.velocity[0] * self.velDamp
        if (
            targetParticle.velocity[1] > self.maxVel
            or targetParticle.velocity[1] < -self.maxVel
        ):
            targetParticle.velocity[1] * self.velDamp
        if (
            targetParticle.force[0] > self.maxForce
            or targetParticle.force[0] < -self.maxForce
        ):
            targetParticle.force[0] = targetParticle.force[0] * self.forceDamp
        if (
            targetParticle.force[1] > self.maxForce
            or targetParticle.force[1] < -self.maxForce
        ):
            targetParticle.force[1] * self.forceDamp
        if targetParticle.pos[0] < 0:
            targetParticle.force[0] -= (targetParticle.pos[0] - 0) * 0.05
        elif targetParticle.pos[0] > self.xMax:
            targetParticle.force[0] -= (targetParticle.pos[0] - self.xMax) * 0.05
        if targetParticle.pos[1] < 0:
            targetParticle.pos[1] = 0
        elif targetParticle.pos[1] > self.yMax:
            targetParticle.force[1] -= (
                targetParticle.pos[1] - self.yMax
            ) * 0.05

    def updateParticle(self):
        timePassed = self.currentTime - self.previousTime
        for targetParticle in self.particles:
            targetParticle.prevPos = targetParticle.pos
            targetParticle.calculateLocation(timePassed)
            targetParticle.force = np.array([0, -1 * self.g])
            self.physicalLimiter(targetParticle)
            targetParticle.rho = targetParticle.rhoNear = 0
            targetParticle.neighbors = []

    def createParticles(self):
        particles = []
        for j in reversed(range(0, self.yMax, ceil(self.supportRadius * 0.5))):
            for i in range(round(self.xMax / 2), self.xMax, ceil(self.supportRadius * 0.5)):
                if len(particles) >= self.numberOfParticles:
                    break
                positionVector = np.array([i, self.yMax - j])
                prevPositionVector = positionVector
                newParticle = Particle(positionVector)
                newParticle.prevPos = prevPositionVector
                particles.append(newParticle)
        self.particles = particles

    def restartSimulation(self):
        self.createParticles()
