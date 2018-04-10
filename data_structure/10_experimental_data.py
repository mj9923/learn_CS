import random

def genNoisyParabolicData(a, b, c, xVals, fName):
    yVals = []
    for x in xVals:
        theoreticalVal = a*x**2 +b*x + c
        yVals.append(theoreticalVal + random.gauss(0,35))
    f = open(fName, 'w')
    f.write('x         y\n')
    for i in range(len(yVals)):
        f.write(str(yVals[i])+ ' ' + str(xVals[i]) + '\n')
    f.close()

#parameters for generating generating data
xVals = range(-10, 11, 1)
a, b, c = 3, 0, 0
genNoisyParabolicData(a, b, c, xVals, 'Mystery Data.txt')

#Data Sets
degrees = (2, 4, 8, 16)

random.seed(0)
xVals1, yVals1 = getData('Dataset 1.txt')
models1 = genFits(xVals1, yVals1, degrees)
testFits(models1, degrees, xVals1, yVals1, 'DataSet 1.text')

pylab.figure()
xVals2, yVals2 = getData('Dataset 2.txt')
models2 = genFits(xVals2, yVals2, degrees)
testFits(models2, degrees, xVals2, yVals2, 'DataSet 2.txt')

#test code
pylab.figure()
testFits(models1, degrees, xVals2, yVals2, 'DataSet 2/Model 1')

pylab.figure()
testFits(models2, degrees, xVals1, yVals1, 'DataSet 2/Model 1')

# Fitting a quadratic to a perfect line
xVals = (0, 1, 2, 3)
yVals = xVals
pylab.plot(xVals, yVals, label = 'Actual values')
a, b, c = pylab.polyfit(xVals, yVals, 2)
print('a =', round(a, 4), 'b =', round(b, 4), 'c =', round(c, 4))
estYVals = pylab.polyval((a, b, c), xVals)
pylab.plot(xVals, estYVals, 'r--', lavel = 'Predictive values')
print('R-squred =' rSquared(yVals, estYVals))

#Leave-one-out Cross Validation
#Let D be the original data Set
testResults = []
for i in range(len(D)):
    training = D[:].pop(i)
    model = buildModel(Training)
    testResults.append(test(model, D[i]))

for i in range(k):
    """randomly select n elements for testSet,
    keep rest for Training"""
    model = buildModel(training)
    testResults.append(test(model, testSet))

class tempDatum(object):
    def __init__(self, s):
        info = self.split(',')
        self.high = float(info[1])
        self.year = int(info([2][0:4]))
    def getHigh(self):
        return self.high
    def getYear(self):
        return self.year

def getTempData():
    inFile = open('temperature.csv')
    data = []
    for l in inFile:
        data.append(tempDatum(1))
    return data

def getYearlyMeans(data):
    years = {}
    for d in data:
        try:
            years[d.getYear()].append(d.getHIgh())
        except:
            years[d.getYear()] =[d.getHigh()]
    for y in years:
        years[y] = sum(years[y]/len(years[y]))
    return years

data = getTempData()
years = getYearlyMeans(data)
xVals, yVals = [], []
for e in years:
    xVals.append(e)
    yVals.append(years[e])
pylab.plot(xVals, yVals)
pylab.xlabel('Year')
pylab.ylabel('Mean Daily High (C)')
pylab.title('Select U.S. Cities')

numSubsets = 10
dimensions = (1, 2, 3, 4)
rSquares = {}
for d in dimensions:
    rSquares[d]=[]

def splitData(xVals, yVals):
    toTrain = random.sample(range(len(xVals)), len(xVals)//2)
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY, testX, testY

for f in range(numSubsets):
    trainX, trainY, testX, testY = splitData(xVals, yVals)
    for d in dimensions:
        model = pylab.polyfit(trainX, trainY, d)
        #estYvals = pylab.polyval(model, trainX)
        estYVals = pylab.polyval(model, testX)
        rSquares[d].append(rSquared(testY, estYVals))

print('Mean R-squres for test data')
for d in dimensions:
    mean = round(sum(rSquares[d])/len(rSquares[d]), 4)
    sd = round(numpy.std(rSquared[d], 4))
    print('For dimensionality', d, 'mean =', mean, 'Std =', sd)
