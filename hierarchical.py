
# heirarichal

# python program to demonstrate the use of heirachial deadlock detection
from collections import defaultdict


class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printgraph(self):
        for i in self.graph:
            print(i, end="->")
            for j in self.graph[i]:
                print(",", j, end=" ")
            print()


n_sites = int(input("Enter the number of sites: "))
site_list = [graph()] * n_sites

# input from user
for i in range(n_sites):
    n = int(input("Enter the number of edges for site {}: ".format(i+1)))
    for j in range(n):
        u, v = map(int, input("Enter the edge (a->b) :").split())
        site_list[i].addEdge(u, v)

# site_list[0].printgraph()


def combine(s1, s2):
    s3 = graph()
    for i in s1.graph:
        for j in s1.graph[i]:
            s3.addEdge(i, j)
    for i in s2.graph:
        for j in s2.graph[i]:
            s3.addEdge(i, j)
    return s3


def dfs(s3, v, visited):
    visited.add(v)
    for i in s3.graph[v]:
        if i not in visited:
            if dfs(s3, i, visited):
                return True
        else:
            return True
    return False

def find_cycle(s3):
    visited = set()
    for i in s3.graph:
        if i not in visited:
            if dfs(s3, i, visited):
                return True
    return False

def detect_deadlock(site_list):
    while len(site_list) > 1:
        local_cordinator = []
        for i in range(0, len(site_list), 2):
            if i+1 < len(site_list):
                local_cordinator.append(combine(site_list[i], site_list[i+1]))
                lc = local_cordinator[-1]
                print(f"Local Coordinator of {i}, {i+1}")
                lc.printgraph()
                if find_cycle(lc):
                    print(f"Deadlock detected at coordinator")
                    lc.printgraph()
                    return
            else:
                local_cordinator.append(site_list[i])
                print("Odd number of sites so this is the last site")
                site_list[i].printgraph()
        site_list = local_cordinator
    print("No deadlock detected")


detect_deadlock(site_list)
