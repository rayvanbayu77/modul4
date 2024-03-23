class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((vertex, neighbor, weight))
    edges.sort(key=lambda edge: edge[2])

    minimum_spanning_tree = []
    disjoint_set = DisjointSet(graph.keys())

    total_cost = 0 

    for edge in edges:
        from_vertex, to_vertex, weight = edge
        if disjoint_set.find(from_vertex) != disjoint_set.find(to_vertex):
            disjoint_set.union(from_vertex, to_vertex)
            minimum_spanning_tree.append(edge)
            total_cost += weight 

    return minimum_spanning_tree, total_cost

graf = {
    'A': {'B': 14, 'D': 12, 'F': 10},
    'B': {'A': 14, 'C': 17, 'D': 20, 'E': 15, 'F': 18},
    'C': {'B': 17, 'E': 13},
    'D': {'A': 12, 'B': 20, 'E': 16, 'F': 11},
    'E': {'B': 15, 'C': 13, 'D': 16, 'F': 11},
    'F': {'A': 10, 'B': 18, 'D': 11, 'E': 11}
}

minimum_spanning_tree, total_cost = kruskal(graf)

print("Jarak terpendek seluruh kota agar dapat dihubungkan:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]} = {edge[2]}")

print(f"Total biaya minimum: {total_cost}")
