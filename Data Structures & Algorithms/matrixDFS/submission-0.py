class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        '''recursive dfs
        '''
        m, n = len(grid), len(grid[0])

        return self.dfs(grid, 0, 0, m, n, set())
    
    def dfs(self, grid, r, c, m, n, visited):
        # base cases
        if (min(r, c) < 0 or
            r == m or c == n or
            grid[r][c] == 1 or # meeting an obstacle
            (r, c) in visited):
            return 0
        
        # reach destination
        if r == m - 1 and c == n - 1:
            return 1 # one path
        
        visited.add((r, c))

        num_paths = 0

        num_paths += self.dfs(grid, r + 1, c, m, n, visited)
        num_paths += self.dfs(grid, r - 1, c, m, n, visited)
        num_paths += self.dfs(grid, r, c + 1, m, n, visited)
        num_paths += self.dfs(grid, r, c - 1, m, n, visited)

        visited.remove((r, c)) # backtrack

        return num_paths
