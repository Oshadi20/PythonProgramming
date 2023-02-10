# Python script to return one of the plausible ordering given a set of tasks 
# and the dependencies among them

from collections import defaultdict

class graph:
    # initialize the graph
    def __init__(self, vertices):
        self.adjacencyList = defaultdict(list) 
        self.Vertices = vertices  # number of vertices in the graph
    
    # add an edge to the adjacencyList representation of graph
    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)
    
    # do Topological Sort and return a list
    def topoSort(self):
        indegreeList = [0]*(self.Vertices) 
        
        for i in self.adjacencyList:
            for j in self.adjacencyList[i]:
                indegreeList[j] += 1
        
        queue = []
        
        for i in range(self.Vertices):
            if(indegreeList[i] == 0):
                queue.append(i)
        
        visited = 0
        tSortList = []
        
        while queue:
            u = queue.pop(0)
            tSortList.append(u)
            for i in self.adjacencyList[u]:
                indegreeList[i] -= 1

                if(indegreeList[i] == 0):
                    queue.append(i)
            visited += 1
        return tSortList
    
# function for count the no of tasks
def countTasks(taskList):
    maxVal = 0
    for dep in taskList:
        for taskNo in dep:
            if(taskNo > maxVal):
                maxVal = taskNo
                
    return maxVal

# read the 'input.txt' file to obtain the set of tasks and their dependencies
file = open("input.txt",'r')
Lines = file.readlines()
taskList = []
for line in Lines:
    splitBySpace = line.split()
    splitByArrow = splitBySpace[1].split("-->")
    splitBySpace[1] = splitByArrow[0]
    temp = []
    temp.append(int(splitBySpace[1]))
    temp.append(int(splitBySpace[2]))
    taskList.append(temp)


n = countTasks(taskList)
G = graph(n)

# add edges to the graph
for dep in taskList:
    G.addEdge(dep[0]-1, dep[1]-1) 

tSortedList = G.topoSort()

tempString = ""
for i in tSortedList:
    tempString = tempString + "task " + str(i+1) + ","

finalString = tempString[:-1]

# resultant sequence is written to a file
eventFile = open("200458.txt","w")
eventFile.write(finalString)
eventFile.close()
