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

def kruskal_with_repair(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((vertex, neighbor, weight))
    edges.sort(key=lambda edge: edge[2])

    minimum_spanning_tree = []
    disjoint_set = DisjointSet(graph.keys())

    total_minimum_cost = 0

    for edge in edges:
        from_vertex, to_vertex, weight = edge
        root1 = disjoint_set.find(from_vertex)
        root2 = disjoint_set.find(to_vertex)

        if root1 != root2:
            minimum_spanning_tree.append(edge)
            disjoint_set.union(from_vertex, to_vertex)
            total_minimum_cost += weight
        elif weight < 0: 
            minimum_spanning_tree.append(edge)
            total_minimum_cost += weight

    return minimum_spanning_tree, total_minimum_cost

graf = {
    'A': {'B': 9, 'D': 10},
    'B': {'A': 9, 'C': 5, 'D': 6, 'E': 5, 'F': 11},
    'C': {'B': 5, 'E': 8},
    'D': {'A': 10, 'B': 6, 'E': 6, 'F': 6},
    'E': {'B': 5, 'C': 8, 'D': 6, 'F': 9},
    'F': {'B': 11, 'D': 6, 'E': 9}
}

minimum_spanning_tree, total_minimum_cost = kruskal_with_repair(graf)

print("Jalur yang bisa diperbaiki dengan biaya minimum tetapi tetap bisa menghubungkan semua kota:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]} = {edge[2]}")

print("Jumlah biaya minimum dari jalur yang bisa diperbaiki adalah:", total_minimum_cost)
