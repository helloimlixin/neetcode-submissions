class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        q.append([0, 0])
        visited.add((0, 0))

        path_len = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == m - 1 and c == n - 1:
                    return path_len
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    r_next, c_next = r + dr, c + dc

                    if (min(r_next, c_next) < 0 or
                        r_next == m or c_next == n or
                        (r_next, c_next) in visited or
                        grid[r_next][c_next] == 1):
                        continue
                    
                    q.append([r_next, c_next])
                    visited.add((r_next, c_next))
            
            path_len += 1 # one layer finished
        
        return -1