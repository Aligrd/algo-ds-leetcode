import random


class Node:
    def __init__(self, v) -> None:
        self.edgeList = []
        self.value = v

    def addEdge(self, edge) -> None:
        self.edgeList.append(edge)


class Edge:
    def __init__(self, n1=None, n2=None, isW=False, w=0) -> None:
        self.startNode = n1
        self.endNode = n2

    def detail(self) -> str:
        return f"startNode:{self.startNode.value} endNode:{self.endNode.value}"

    # every edge need 2 node
    def addNode(self, node1, node2=None) -> None:
        self.startNode = node1
        self.endNode = node2


class Graph:
    def __init__(self):
        self.NodeList = []
        self.EdgeList = []
        pass

    def addNode(self, value) -> None:
        newNode = Node(value)
        self.NodeList.append(newNode)
        return newNode

    def addEdge(self, startVertex: Node, endVertex: Node = None) -> Edge:
        newEdge = Edge(startVertex, endVertex)
        startVertex.addEdge(newEdge)
        endVertex.addEdge(newEdge)
        self.EdgeList.append(newEdge)
        return newEdge

    def printGraph(self) -> None:
        # algorithm to print graph
        print()


class graphAlgo:
    def __init__(self, g: Graph) -> None:
        self.graph = g

    def dfs(self):
        Nodes: list[Node] = self.graph.NodeList
        rndNode: Node = random.choice()  # itnial node in the graph
        edges: list[Node] = rndNode.edgeList
        stack = []
        visited = []

        for edge in edges:
            edge
        # dfs work with stack

    def bfs(self, vertex: Node):
        # dfs work with queue
        pass

    def dikistra(self, vertex: Node):
        # dikistra work with priority queue
        pass


g = Graph()
node1 = g.addNode(10)
node2 = g.addNode(121)
g.addEdge(node1, node2)
for i in g.NodeList:
    print(i.value)
    for edge in i.edgeList:
        print(edge.detail())
