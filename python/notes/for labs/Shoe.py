class Shoe:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def getType(self):
        return "shoes"

    def describe(self):
        return "{} {}: size {}".format(self.color, self.getType(), self.size)


class Boots(Shoe):
    def __init__(self, color, size, height):
        super().__init__(color, size)
        self.height = height

    def getType(self):
        return "boots"

    def describe(self):
        return "{} height: {}".format(super().describe(), self.height)


class Sneakers(Boots):
    def __init__(self, color, size, height, lace_color):
        super().__init__(color, size, height)
        self.lace_color = lace_color

    def getType(self):
        return "sneakers"

    def describe(self):
        return "{} lace color: {}".format(super().describe(), self.lace_color)


print(".", end="")
