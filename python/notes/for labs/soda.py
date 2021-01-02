import math


class SodaCan:
    height = 0
    radius = 0

    def setHeight(self, height):
        self.height = height

    def setRadius(self, radius):
        self.radius = radius

    def getSurfaceArea(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)

    def getVolume(self):
        return math.pi * (self.radius ** 2) * self.height


soda1 = SodaCan()
soda1.setHeight(int(input("Choose a height")))
soda1.setRadius(int(input("Choose a radius")))
print(soda1.getSurfaceArea())
print(soda1.getVolume())




