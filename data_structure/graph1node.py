class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name= name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    """Assumes src and dest are nodes"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName()+ '->' + self.dest.getName()

class weightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """Assumes src and dest are nodes, weight a number"""
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')' + self.dest.getName()
        self.arg = arg

class Digraph(object):
    #nodes is a list of the nodes in the Digraph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node]=[]
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edge[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'+dest.getName() +'\n'
        return result [:-1] #omit final new line

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getsource())
        Digraph.addEdge(self, rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.addEdge(Edge(g.getNode('Boston'), g.getNode('Province')))
        g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
        g.addEdge(Edge(g.getNode('Province'), g.getNode('Boston')))
        g.addEdge(Edge(g.getNode('Province'), g.getNode('New York')))
        g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
        g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
        g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
        g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
        g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
        g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
        return g

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
    path and shortest are lists of nodes
    Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS (graph, node, end, path, shortest, toPrint)
            if newPath != None:
                shortest = newPath
    return shortest

def shortestPath(graph, start, end, toPrint = False):
    """Assumes graph is Digraph; start and end are nodes
    Returns a shortest path from start to end in graph"""
    return DFS(grpah, start, end, [], None, toPrint)

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to', destination)

testSP('Bostn', 'Chicago')

def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None
