class Graph:
    def __init__(self):
        self.graph = {}  

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def dfs(self, start):
        visited = set()  
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        if node not in visited:
            print(node, end=" ")  
            visited.add(node)  
            for neighbor in self.graph.get(node, []): 
                self._dfs_helper(neighbor, visited)

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(5, 6)

print("DFS Traversal starting from node 1:")
graph.dfs(1)


