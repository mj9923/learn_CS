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
