#centralized

from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def printgraph(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(f"{i}->{j}")
        print()

s1 = graph()
s2 = graph()

n1 = int(input("Enter number of edge in graph 1 : "))
n2 = int(input("Enter number of edge in graph 2 : "))

for i in range(n1):
    u,v = map(int,input("Enter u and v where u->v : ").split())
    s1.addedge(u,v)

for i in range(n2):
    u,v = map(int,input("Enter u and v where u->v : ").split())
    s2.addedge(u,v)

def combine(s1,s2):
    s3 = graph()
    for i in s1.graph:
        for j in s1.graph[i]:
            if j not in s3.graph[i]:
                s3.addedge(i,j)
    for i in s2.graph:
        for j in s2.graph[i]:
            if j not in s3.graph[i]:
                s3.addedge(i,j)
    return s3

def dfs(i,s,visited):
    visited.add(i)
    for j in s.graph[i]:
        if j not in visited:
            if dfs(j,s,visited):
                return True
        else:
            return True
    return False
    

def findcycle(s):
    # print(1)
    for i in list(s.graph.keys()):
        # print(s.graph)
        # print(2)
        if dfs(i,s,set()):
            return True
    return False

s3 = combine(s1,s2)
s1.printgraph()
if findcycle(s3):
    print("Dedlock bound")
else:
    print("No dedlock bound")