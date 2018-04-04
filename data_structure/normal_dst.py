import random
dist, numSamples = [], 1000000

for i in range(numSamples):
    dist.append(random.gauss(0, 100))

weights = [1/numSamples]*len(dist)
v = pylab.hist(dist, bins = 100, weights = [1/numSamples]*len(dist))
pylab.xlabel('x')
pylab.ylabel('Relative Frequency')

print('Fraction within ~200 of mean =', sum(v[0][30:70]))

# normal distribution function
def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2/(2*sigma**2)))
    return factor1*factor2

xVals, yVals = [], []
mu, sigma = 0, 1
x= -4
while x <= 4:
    xVals.append(x)
    yVals.append(gaussian(x, mu, sigma))
    x += 0.05
pylab.plot(xVals, yVals)
pylab.title('Normal Distribution, mu = ' str(mu) + ', sigma = ' + str(sigma))

import scipy.integrate

def cehckEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma = ', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian, mu-numStd*sigma, mu+numStd*sigma, (mu, sigma))[0]
            print(' Fraction within', numStd, 'std =', round(area, 4))

def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend, weights = pylab.array(len(means)*[1])/len(means), hatch = style)
    return getMeanAndStd(means)

mean, std = plotMeans(1, 1000000, 19, ' 1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
mean, std = plotMeans(50, 10000000, 19, 'Mean of 50 dice', 'r', '//')
pylab.title('Mean of rolling 50 dice =', str(mean)+',', 'Std =', std)
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()

#simulatin buffon-Laplace Method
def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle +=1
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(curEst) + ', Std. dev. =' + str(round(sDev, 6)) + ', Needles = ' + str(numNeedles))
    return(curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEst(numNeedles, numTrials)

        numNeedles *= 2
    return curEst
estPi(0.005, 1008)
