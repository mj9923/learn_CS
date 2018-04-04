#how to make errorbar
pylab.errorbar(xVals, sizeMeans, yerr=1.96*pylab.array(sizeSDs), fmt='o', label = '95% Confidence Interval')

#testing the SEM
sampleSizes = (25, 50, 100, 200, 300, 400, 500, 600)
numTrials = 50
population = getHighs()
popSD = numpy.std(population)
sems = []
sampleSDs = []
for size in sampleSizes:
    sems.append(sem(popSd, size))
    means = []
    for t in range(numTrials):
        sample = random.sample(population, size)
        means.append(sum(sample)/len(sample))
    sampleSDs.append(numpy.std(means))
pylab.plot(sampleSizes, sampleSDs, label = 'Std of ' + str(numTrials) + ' means')
pylab.plot(sampleSizes, sems, 'r--', label = 'SEM')
pylab.xlabel('Sample Size')
pylab.ylabel('Std and SEM')
pylab.title('SD for ' + str(numTrials) + ' Means and SEM')
pylab.legend()

#Distribution
def plotDistributions():
    uniform, normal, exp = [], [], []
    for i in range(100000):
        uniform.append(random.random())
        normal.append(random.gauss(0, 1))
        exp.append(random.expovariate(0.5))
    makeHist(uniform, 'Uniform', 'Value', 'Frequency')
    pylab.figure()
    makeHist(normal, 'Gaussian', 'Value', 'Frequency')
    pylab.figure()
    makeHist(exp, 'Exponential', 'Value', 'Frequency')

#Are 200 samples enough?
 numBad = 0
 for t in range(numTrials):
     sample = random.sample(temp, sampleSize)
     sampleMean = sum(sample)/sampleSize
     se = numpy.std(sample)/sampleSize**0.5
     if abs(popMean - sampleMean) > 1.96*se:
         numBad += 1
print('Fraction outside 95% confidence interval =', numBad/numTrials)
