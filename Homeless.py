import random

class Homeless:

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def posicion(self):
        return(self.x, self.y)

    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5

class StandardHomeless(Homeless):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        dx, dy =  random.choice([(0, 2), (0, -2), (2, 0), (-2, 0)])
        self.x += dx
        self.y += dy
        return [self.x, self.y]

class ModerateHomeless(Homeless):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-5,0)])
        self.x += dx
        self.y += dy
        return [self.x, self.y]

class LeftHomeless(Homeless):

    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-5,0)])
        self.x += dx
        self.y += dy
        return [self.x, self.y]

class RightHomeless(Homeless):

    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        dx, dy = random.choice([(0,5), (0,-1), (5,0), (-1,0)])
        self.x += dx
        self.y += dy
        return [self.x, self.y]