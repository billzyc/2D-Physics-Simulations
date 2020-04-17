import math


class Projectile:
    def __init__(self, width):
        self.velocityX = 0
        self.velocityY = 0
        self.velocity = 0
        self.initialVelocityX = 0
        self.initialVelocityY = 0
        self.initialVelocity = 0
        self.angle = 0
        self.width = width

    def setVelocity(self, initialVelocity):
        self.initialVelocity = self.velocity = initialVelocity
        self.initialVelocityX = self.velocityX = (
            math.cos(self.angle * math.pi / 180) * self.initialVelocity
        )
        self.initialVelocityY = self.velocityY = (
            math.sin(self.angle * math.pi / 180) * self.initialVelocity
        )

    def setAngle(self, initialAngle):
        self.angle = initialAngle

    def promptProjectileCondition(self):
        initialVelocity = int(
            input("enter the velocity of the initial Projectile in m/s: ")
        )
        initialAngle = int(
            input(
                "enter the degree of the initial Projectile in degrees above the horizon: "
            )
        )
        self.setAngle(initialAngle)
        self.setVelocity(initialVelocity)

    def velocityKinematicFormula(self, initialVelocity, time, acceleration):
        return initialVelocity + acceleration * time

    def calculateCurrentVelocity(self, time, resistanceX, resistanceY):
        self.velocityX = self.velocityKinematicFormula(
            self.initialVelocityX, time, resistanceX
        )
        self.velocityY = self.velocityKinematicFormula(
            self.initialVelocityY, time, resistanceY
        )
        self.velocity = math.sqrt(self.velocityX ** 2 + self.velocityY ** 2)
        # print(f"current velocity: {self.velocity} m/s")
