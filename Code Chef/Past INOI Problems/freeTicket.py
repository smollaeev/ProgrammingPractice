from collections import defaultdict
import copy

class Graph:   
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list) 
        self.costs = defaultdict (list)
        self.paths = []
   
    def addEdge(self, u, v, cost):
        self.graph[u].append(v)
        self.costs [f'{u},{v}'].append (cost)

    def find_AllPathsUtil(self, u, d, visited, path):
        visited[u - 1]= True
        path.append(u)
        if u == d:
            self.paths.append (copy.deepcopy (path))
        else:
            for i in self.graph[u]:
                if visited[i - 1]== False:
                    self.find_AllPathsUtil(i, d, visited, path)
        path.pop ()
        visited[u - 1]= False

    def find_AllPaths(self, s, d):
        visited =[False]*(self.V)
        path = []
        costs = []
        self.find_AllPathsUtil(s, d, visited, path)
        for i in range (len (self.paths)):
            c = 0
            for j in range (len (self.paths [i]) - 1):
                c += self.costs [f'{self.paths [i][j]},{self.paths [i][j + 1]}'][0]
            costs.append (c)
        return costs

def find_RoutesCosts (i , j, C, flights):
    g = Graph(C)
    for f in flights:
        g.addEdge (f [0], f [1], f [2])
        g.addEdge (f [1], f [0], f[2])

    routesCosts = g.find_AllPaths (i, j)
    return routesCosts    


def find_CheapestCosts (C, flights):
    cheapest = []
    for i in range (1, C + 1):
        for j in range (i + 1 , C + 1):
            routesCosts = find_RoutesCosts (i, j, C, flights)
            cheapest.append (min (routesCosts))
    return cheapest

def maximize_CheapestCost (C, flights):
    cheapest = find_CheapestCosts (C, flights)
    return max (cheapest)

firstLineStr = input ()
firstLineListStr = firstLineStr.split ()
if len (firstLineListStr) != 2:
    exit ()

firstLineList = list (map (int, firstLineListStr))
C = firstLineList [0]
F = firstLineList [1]

flightsStr = []
flights = []
for line in range (F):
    flightsStr.append (input ())
    flights.append (list (map (int , flightsStr [line].split ())))
    if len (flights [line]) != 3:
        exit ()
    if flights [line][0] == flights [line][1]:
        exit ()
for line in range (len (flights)):
    for i in range (line + 1, len (flights)):
        if (flights [line][0] == flights [i][0] and flights [line][1] == flights [i][1]) or (flights [line][1] == flights [i][0] and flights [line][0] == flights [i][1]):
            exit ()

print (maximize_CheapestCost (C, flights))