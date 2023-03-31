class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = { vertex: [] for vertex in vertices }
        self.edges = []
        
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
        self.edges.append((u, v, weight))
                 
    def kruskal(self):
        mst = []
        disjoint_set = {vertex: set(vertex) for vertex in self.vertices}
        sorted_edges = sorted(self.edges, key=lambda edge: edge[2]) # Sort by weights, increasing order
        
        for u, v, weight in sorted_edges:
            if disjoint_set[u].isdisjoint(disjoint_set[v]):
                mst.append((u, v, weight))
                disjoint_set = self._union(disjoint_set, u, v)
                if len(mst) == len(vertices) - 1:
                    break
        return mst
                
    def _union(self, disjoint_set, u, v):
        if len(disjoint_set[u]) > len(disjoint_set[u]):
            disjoint_set[u] = disjoint_set[u].union(disjoint_set[v])
        else:
            disjoint_set[v] = disjoint_set[v].union(disjoint_set[u])
        return disjoint_set
        


if __name__ == '__main__':
    vertices = ['a', 'b', 'c', 'd', 'e']
    graph = Graph(vertices=vertices)
    graph.add_edge('a', 'b', 5)
    graph.add_edge('b', 'd', 6)
    graph.add_edge('a', 'c', 3)
    graph.add_edge('c', 'd', 2)
    graph.add_edge('d', 'e', 8)
    mst = graph.kruskal()
    print(mst)