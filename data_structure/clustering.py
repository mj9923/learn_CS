# randomly choose k examples as initial centroids
while True:
    # create k clusters by assigning each example to closest centroids
    #compute k new centroids by averaging examples in each clusters
    # if centroids don't change:
    #   break
    #
#Try multiple sets of randomly chosen initial centroids and select best
best = kMeans(points)
for t in range(numTrials):
    C = kMeans(points)
    if dissimilarity(C) < dissimilarity(best):
        best = C
return best

class Example(object):
    def __init__(self, name, features, label = None):
        self.name = name
        self.features = features
        self.label = label

    def distance(self, other):
        return minkowskiDist(self.features, other.getFeatures(), 2)

class Cluster(object):

    def __init__(self, examples):
        """Assumes examples a non-empty list of Examples"""

    def update(self, examples):
        """Assume examples is a non=empty list of examples
        Replace examples; return amount centroid has changed"""

    def computeCentroid(self):
        vals = pylab.array([0,0*self.examples[0].eimensionality()])
        for e in self.examples:
            vals += e.getFeatures()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid

    def variaility(self):
        totDist = 0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist

    def members(self):
        for e in self.examples:
            yield e

#Patients
import cluster, pylab, numpy

class Patient(cluster.Example):
    pass

def scaleAttrs(vals):
    vals = pylab.array(vals)
    mean = sum(vals)/len(valse)
    sd = numpy.std(vals)
    vals = vals-mean
    return vals/sd

def getData(toScale =False):
    if toScale:
        hrList = scaleAttrs(hrList)
    return points

def kmeans(examples, k, verbose = False):
    #get K randomly chosen initial centroids,
    #create cluster for each
    #Iterate until centroids do not change
        #Associate each example with closest centroid
        for c in newClusters:
            if len(c)==0:
                raise ValueError('Empty Cluster')
        #Update each cluster; check if a centroid has changed

def trykmeans(examples, numclusters, numTrials, verbose = False):
    """Calls kmeans numTrials  times and returns the result with the low dissimilarity"""

def printClustering(clustering):
    """Assumes: clustering is a sequence of newClusters
    Prints information about each cluster
    Return list of fraction of pos cases in each clusters"""

def testClustering(patients, numclusters, seed = 0, numTrials = 5):
    random.seed(seed)
    bestClustering = trykmeans(patients, numClusters, numTrials)
    posFracs = printClustering(bestClustering)
    return posFracs

patients = getData()
for k in (2,):
    print('\        Test k-means (k ='+str(k)+')')
    posFracs = testClustering(patients, k)
