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


def minimum_spanning_tree(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    total_cost = 0

    for edge in edges:
        u, v, cost = edge
        if uf.find(u - 1) != uf.find(v - 1):
            uf.union(u - 1, v - 1)
            total_cost += cost

    return total_cost


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    result = minimum_spanning_tree(n, edges)

    if result == 0:
        print("IMPOSIBLE")
    else:
        print(result)


if __name__ == "__main__":
    main()
