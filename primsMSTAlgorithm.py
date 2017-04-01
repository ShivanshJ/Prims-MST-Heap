import sys
from heap import Heap
import csv

class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self
        self.indexy=[]   #MINE.....for making an array of all
                        #unique points in the cluster sent.
        self.adjList={}
        self.edgeList={}
        self.edgeID = 0

    def unique(self, u):
        self.indexy.append(u)

    def convert_point_index(self, u, v, w):     
        self.addEdge(self.indexy.index(u), self.indexy.index(v),w)

    def addEdge(self,u,v,w):
        '''
        Builds an adjacency list and an incidence list

        Args:
                filename: the name of the file with a representation of the graph. The first line of the file specifies
                                  the number of the vertices and the number of the edges. The file is assumed to specify
                                  the edges of the graph in the following format: v w e, where v is one vertex of the
                                  associated edge, w is the other vertex, and e is the edge's weight
        
        Returns:
                adjList: a dictionary, as a realization of an adjacency list, in the form
                                 adjList[vertex1] = [(vertex21,weight1,edgeId1), (vertex22,weight2,edgeId2), ...]
                edgeList: a dictionary, as a realization of an incidence list, in the form
                                  edgeList[edgeId] = (vertex1,vertex2,weight)
        '''

    
        numVertices = self.V
        
        #edgeID = 1

        vertex1, vertex2, weight = u,v,w
        
        if vertex1 in self.adjList: self.adjList[vertex1].append((vertex2,weight,self.edgeID))
        else: self.adjList[vertex1] = [(vertex2,weight,self.edgeID)]
        if vertex2 in self.adjList: self.adjList[vertex2].append((vertex1,weight,self.edgeID))
        else: self.adjList[vertex2] = [(vertex1,weight,self.edgeID)]
        
        self.edgeList[self.edgeID] = (vertex1,vertex2,weight)
        self.edgeID += 1

        numEdges = self.edgeID

        
    def primsMSTAlgorithm(self):
        '''
        Prim's Minimum Spanning Tree (MST) Algorithm 

        It finds a MST of an undirected graph

        Args:
                adjList: a dictionary, as a realization of an adjacency list, in the form
                                 adjList[vertex1] = [(vertex21,weight1,edgeId1), (vertex22,weight2,edgeId2), ...]
                                 Note: Every vertex should have an entry in the adjList

        Returns:
                mst: a set of all the edges (ids) that constitute the minimum spanning tree
        '''
        
        def updateHeap(v):
            '''
            Updates the heap with entries of all the vertices incident to vertex v that was recently explored

            Args:
                    v: a vertex that was recently explored
            '''
            for vertex,weight,edgeID in self.adjList[v]:
                if vertex not in explored:
                    # Updates (!) the weight and reinserts the element into the heap
                    element = unexplored.delete(vertex)
                    if element and element[0] < weight: unexplored.insert(element)
                    else: unexplored.insert((weight,vertex,edgeID))


        source = list(self.adjList.keys())[0]  # Chooses an arbitrary vertex as the starting point of the algorithm
        # unexplored: a heap with elements of the following format (minWeight, destinationVertex, edgeID)
        unexplored, explored, mst = Heap(), set([source]), set()
        updateHeap(0)

        #for i in range(1,len(self.edgeList)) :
         #       print self.edgeList[i][0],self.edgeList[i][1],self.edgeList[i][2]
            
        result=[]
        while unexplored.length():
            weight, vertex, edgeID = unexplored.extractMin()
            explored.add(vertex)
            ##........................edgeID has - index(u) , index(v) , w
            ##........................result appends - u,v,w
            #here self.indexy not seen
            result.append([  self.edgeList[edgeID][0] ,  self.edgeList[edgeID][1] , self.edgeList[edgeID][2] ]) 
            updateHeap(vertex)
        
        return result #has u,v,w

##g is the object of the class Graph(v) , where v is the number of nodes/vertices
#Here, v is 9, i.e, vertices numbered (0 to 8)/(1 to 9), here (0 to 8) format is taken
g = Graph(9)        
g.addEdge(0, 1,  4)
g.addEdge(0, 7, 8)
g.addEdge(1, 7, 11)
g.addEdge(1, 2, 8)
g.addEdge(2, 8, 2)
g.addEdge(2,5,4)
g.addEdge(2,3,7)
g.addEdge(3,4,9)
g.addEdge(3,5,14)
g.addEdge(4,5,10)
g.addEdge(5,6,2)
g.addEdge(6,7,1)
g.addEdge(6,8,6)
g.addEdge(7,8,7)

result=g.primsMSTAlgorithm()

print 'Edges of the MST are: '
cost=0
for u,v,w in result:
    print '%d -- %d : %d ' % (u,v,w)
    cost += w
print 'Cost :', cost
print '\nxxxxxxxxxxxxxxxxxxxxxxxx'

#...................................
g = Graph(4)
g.addEdge(0, 3,  1)
g.addEdge(0, 1, 8)
g.addEdge(1, 2, 2)
g.addEdge(1, 3, 5)
g.addEdge(2, 3, 6)

result=g.primsMSTAlgorithm()

print 'Edges of the MST are: '
cost=0
for u,v,w in result:
    print '%d -- %d : %d ' % (u,v,w)
    cost += w
print 'Cost :', cost
