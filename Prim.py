import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = { vertex: [] for vertex in vertices }
        self.edges = []
        
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
        self.edges.append((u, v, weight))
                 
    def prim(self, starting_vertex):
        mst = []
        pq = []
        visited = { vertex: False for vertex in self.vertices }
        heapq.heappush(pq, (0, starting_vertex))
        
        while len(pq) > 0:
            w, v = heapq.heappop(pq)
            print((w, v))
            if not visited[v]:
                visited[v] = True
                mst.append((v, w))
                for neighbor, weight in self.adj_list[v]:
                    if not visited[neighbor]:
                        heapq.heappush(pq, (weight, neighbor))
        return mst


if __name__ == '__main__':
    vertices = ['a', 'b', 'c', 'd', 'e']
    graph = Graph(vertices=vertices)
    graph.add_edge('a', 'b', 5)
    graph.add_edge('b', 'd', 6)
    graph.add_edge('a', 'c', 3)
    graph.add_edge('c', 'd', 2)
    graph.add_edge('d', 'e', 8)
    mst = graph.prim('a')
    print(mst)