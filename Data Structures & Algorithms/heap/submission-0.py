class MinHeap:
    
    def __init__(self):
        self.heap = [0] # dummy value for easier arithmic

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) <= 1: # equal is also okay
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        root = self.heap[1]

        self.heap[1] = self.heap.pop() # overwrite with the last value
        self._percolate_down(1)
        return root

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        # do percolate down for all nodes (essentially top half)
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._percolate_down(i)
    
    def _percolate_up(self, index):
        parent = index // 2 # thanks to the dummy value

        while index > 1 and self.heap[index] < self.heap[parent]:
            # swap
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2
    
    def _percolate_down(self, index):
        # swap with lesser child
        child = 2 * index # left, right = child + 1

        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                # right child is smaller
                child += 1
            if self.heap[child] >= self.heap[index]:
                return
            
            # take care of both cases (left or right smaller)
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = 2 * index # left child
