import random
import pylab

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

class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are numbers"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x -ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

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

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        #use move method of location to get new location
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps as int >= 0
    Moves d numSteps times; returns the distance between the final
    location and the location at the start of the walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))



def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk
    Simulates numTrials walks of numSteps steps each. Returns a list of the final distances for each trial"""
    Homer = dClass()
    origin = Location(0,0)
    distances = []
    for t  in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numTrials), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """ Assume walkLengths a sequence of ints >= 0
    numTrials an int >0
    dClass a subclass of Drunk
    for each number of steps in walkLengths,
    runs simWalks with numTrials walks and print results"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print('Mean =', round(sum(distances)/len(distances), 4))
        print('Max =', max(distances), 'Mean =', min(distances))

class OddField(Field):
    def __init__(self, numHoles = 1000, xRange = 100, yRange = 100):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x,y)] = newLoc

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
    pylab.title('Mean Distance from Origin(' + str(numTrials) + 'trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
