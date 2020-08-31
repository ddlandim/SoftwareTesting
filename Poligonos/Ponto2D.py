import math
class Ponto2D(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self, x):
        return self.x

    def getY(self, y):
        return self.y

    def calcDistance(p1,p2):
        distX = abs(p1.x - p2.x)
        distY = abs(p1.y - p2.y)
        return math.sqrt(distX^2 + distY^2);