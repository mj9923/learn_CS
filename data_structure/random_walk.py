import random

class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)

class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class Field(object):
    def __init__(self):
        self.drunks ={}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunks')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def moveDruk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        #use move method of location to get new location
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

    def simWalks(numSteps, numTrials, dClass):
        """Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk
        Simulates numTrials walks of numSteps steps each. Returns a list of the final distances for each trial"""
        Homer = dClass()
        origin = Location(0,0)
        distances = []
        for t  in rante(numTrials):
            f = Field()
            f.addDrunk(Homer, origin)
            distances.append(round(walk(f, Homer, numtrials), 1))
        return distances
