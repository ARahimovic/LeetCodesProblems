from collections import defaultdict, deque

def count_componenets(n , edges):
#we first consutrcut the graph

    graph = defaultdict(list)

    for u,v in edges :
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    component_count = 0

    for start in range(n):
        if start in visited :
            continue

        component_count += 1
        visited.add(start)
        queue = deque([start])

        while queue :
            node = queue.popleft()
            
            for neighbour in graph[node] :
                if neighbour not in visited :
                    visited.add(neighbour)
                    queue.append(neighbour)

    return component_count
       
            
edges = [(0,1),(0,2),(1,2),(2,3),(4,5),(5,6),(7,8)]
print(count_componenets(10, edges)) 



    