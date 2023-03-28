# probe

def detect_deadlock(n, links):
    graph = {}
    for i in range(n):
        graph[i] = []
    
    for (initial, sender, receiver) in links:
        graph[sender].append(receiver)
        print(graph)
    
    visited = [False] * n
    rec_stack = [False] * n
    
    def is_deadlocked(v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        
        for i in graph[v]:
            #print("inside func {}".format(i))
            if not visited[i]:
                if is_deadlocked(i, visited, rec_stack):
                    return True
            elif rec_stack[i]:
                return True
        
        rec_stack[v] = False
        return False
    
    for i in range(n):
        #print(i)
        if not visited[i]:
            if is_deadlocked(i, visited, rec_stack):
                return True
    
    return False

if __name__ == '__main__':
    n = int(input("Enter the number of processes: "))
    links = []
    for i in range(n):
        initial, sender, receiver = map(int, input("Enter the initial, sender, and receiver process for link {}: ".format(i+1)).split())
        links.append((initial, sender, receiver))
    
    result = detect_deadlock(n, links)
    if result:
        print("Deadlock detected")
    else:
        print("No deadlock detected")

