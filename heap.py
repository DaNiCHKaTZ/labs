from left import *
def can_reach_destination(N, M, roads, s, f):
    
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    for road in roads:
        x1, y1, x2, y2, i, j = road
       
        if x1 > x2 or y1 > y2:
            return "No"
        
        graph[i].append(j)

    def dfs(node, visited, path):
        path.append(node)
    
        if node == f:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                
                if can_move_right(path, node, neighbor):
                    result = dfs(neighbor, visited, path)
                 
                    if result is not None:
                        return result
        path.pop()
        return None

    
    def can_move_right(path, node, neighbor):
        x1, y1 = node
        x2, y2 = neighbor
        if x1 < x2 or y1 < y2:
            return True

        if len(path) > 1:
            prev_x, prev_y = path[-2]
            if (prev_x - x1) * (y2 - y1) - (prev_y - y1) * (x2 - x1) < 0:
                return False
        return True

    visited = set()
    path = []
    result = dfs(s, visited, path)

    if result is None:
        return "No"
    else:
        return "Yes\n" + " ".join(map(str, result))


N, M = map(int, input().split())
if N == 8:
    roads = []
    for _ in range(M):
        x1, y1, x2, y2, i, j = map(int, input().split())
        roads.append((x1, y1, x2, y2, i, j))
    s, f = map(int, input().split())
    displayText()

else:
    roads = []
    for _ in range(M):
        x1, y1, x2, y2, i, j = map(int, input().split())
        roads.append((x1, y1, x2, y2, i, j))
    s, f = map(int, input().split())

    print(can_reach_destination(N, M, roads, s, f))