class Graph:
    
    def __init__(self):
        self.adjacency_list = {} # src -> set() of neighbors

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjacency_list:
            self.adjacency_list[src] = set()
        if dst not in self.adjacency_list:
            self.adjacency_list[dst] = set()
        
        self.adjacency_list[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjacency_list or dst not in self.adjacency_list[src]:
            return False
        
        self.adjacency_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)
    
    def dfs(self, src, dst, visited):
        if src == dst:
            return True
        
        visited.add(src)

        for neighbor in self.adjacency_list.get(src, set()):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
        return False
