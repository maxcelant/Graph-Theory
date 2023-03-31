class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = { vertex: [] for vertex in vertices }
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def dfs(self):
        visited = set()
        
        def _dfs(node):
            if node is None:
                return
            print(node)
            visited.add(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    _dfs(neighbor)
        
        _dfs(vertices[0])
             


if __name__ == '__main__':
    vertices = ['a', 'b', 'c', 'd', 'e']
    graph = Graph(vertices=vertices)
    graph.add_edge('a', 'b')
    graph.add_edge('b', 'd')
    graph.add_edge('a', 'c')
    graph.add_edge('c', 'd')
    graph.add_edge('d', 'e')
    graph.dfs()