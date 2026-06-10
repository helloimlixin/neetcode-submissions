class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}

        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n
        

    def find(self, x: int) -> int:
        '''find the root parent of x
        '''
        if x != self.parent[x]:
            # path compression by recursion
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        '''connect x and y'''
        root_x, root_y = self.find(x), self.find(y)

        # union by size
        if root_x == root_y:
            return False

        if self.size[root_x] > self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        elif self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += 1
        self.num_components -= 1  # decrement the number of components after each union
        return True

    def getNumComponents(self) -> int:
        return self.num_components
