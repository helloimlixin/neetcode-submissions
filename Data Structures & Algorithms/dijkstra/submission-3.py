class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        """bfs shortest path: edges without weights
        edges with weights (no negative weights) -> dijkstra

        node   0   1   2   3   4
        weight 0   7   3   9   5

        to find the min sum of path costs, we might need an MinHeap
        <weight, node>

        Condier the connected graph represented by adjacency lists:
            - edge[0]: src
            - edge[1]: dst
            - edge[2]: weight
        
        Goal: find the shortest path from src to every other node in the
            graph. There are n nodes in the graph.
        
        Dijkstra: greedy breadth-first search
        
        Time complexity: O(E * log V).
        """
        # take the edges and convert to adjacency lists
        adjacency_list = {}
        for i in range(n):
            adjacency_list[i] = []
        
        for s, t, weight in edges:
            adjacency_list[s].append([t, weight])
        
        shortest_path = {}  # map vertices -> distances of shortest paths

        minHeap = [(0, src)]  # a starting point for bfs, the Dijkstra algorithm is a
                              # greedy breadth-first algorithm, i.e., for every vertex
                              # we will always take the edges that will have the total
                              # shortest paths, which can be implemented using a minheap

        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in shortest_path:  # check if seen eaarlier
                continue
            shortest_path[node1] = weight1

            for node2, weight2 in adjacency_list[node1]:
                if node2 not in shortest_path:  # avoid infinite loops
                    heapq.heappush(minHeap, (weight1 + weight2, node2))
        
        # for unvisited nodes
        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1  # we are supposed to set these nodes to weights of -1 indicating not visited
        
        return shortest_path

