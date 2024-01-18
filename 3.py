class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1


def minimum_roads(n, roads):
    uf = UnionFind(n)
    required_roads = []

    for road in roads:
        a, b = road
        if uf.find(a - 1) != uf.find(b - 1):
            required_roads.append((a, b))
            uf.union(a - 1, b - 1)

    return required_roads


# Lectura de entrada
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

# Calcular caminos mínimos necesarios
result = minimum_roads(n, roads)

# Imprimir salida
print(len(result))
for road in result:
    print(*road)
