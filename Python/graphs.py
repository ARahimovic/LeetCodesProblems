mygraph = {
    "A" : ["B" , "C"],
    "B" : ["A", "D"],
    "C" : ["A", "D"],
    "D" : ["B", "C"]
}

# build an adjaency list using list of list
n = 5
edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 4]
]

graph = [[] for _ in range(5)]

for u, v in edges :
    graph[u].append(v)
    graph[v].append(u)

print(graph)


from collections import defaultdict
## build adjency list using hasmap
edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 4]
]

graph_hasmap = defaultdict(list)

for u,v in edges :
    graph_hasmap[u].append(v)
    graph_hasmap[v].append(u)

print(graph_hasmap)


### build matrix from edge list
n = 5
matrix = [[0] * n for _ in range(n) ]

for u,v in edges :
    matrix[u][v] = 1
    matrix[v][u] = 1

print(matrix)


from collections import deque
def bfs(graph, start) :
    visited = set()
    queue = deque([start])
    visited.add(start)

    traversal_order = []

    while queue :
        node = queue.popleft()
        traversal_order.append(node)

        for neighbour in graph[node] :
            if neighbour in visited :
                continue
            
            visited.add(neighbour)
            queue.append(neighbour)

    return traversal_order



#DFS iterative


def DFS(graph, start) :
    visited = set()
    stack = [start]
    traversal = []

    while stack :
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            print(node)

            for neighbour in reversed(graph[node]) :
                if neighbour not in visited :
                    stack.append(neighbour)
                
    return traversal


print(f"DFS {DFS(mygraph,"A")}")

# #we need to use queue
# from collections import deque
# def BFS(graph , start) :

#     visited = set()
#     queue = deque([start])

#     visited.add(start)

#     while queue :
#         node = queue.popleft()
#         print(node)

#         for neighbour in graph[node] :
#             if neighbour in visited :
#                 continue 
            
#             visited.add(neighbour)
#             queue.append(neighbour)


print(bfs(mygraph, "A"))



def has_path(graph, start, end):
    visited = set()
    stack = [start]

    while stack :
        node = stack.pop()

        if node == end :
            return True

        if node not in visited :
            visited.add(node)

            for neighbour in reversed(graph[node]) :
                if neighbour not in visited:
                    stack.append(neighbour)
    
    return False


def has_path_BFS(graph, start, end):
    if start == end :
        return True

    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue :
        current = queue.popleft()
        if current == end :
            return True

        for neighbour in graph[current] :
            if neighbour not in visited :
                visited.add(neighbour)
                queue.append(neighbour)
    
    return False



def shortest_path(graph, start, end):
    if start == end :
        return 0

    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)

    while queue :
        node, dist = queue.popleft()

        if node == end :
            return dist
        
        for neighbour in graph[node] :
            if neighbour not in visited :
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))
    
    return dist

    
    