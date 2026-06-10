class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        '''amortized O(1) complexity
        '''
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # soft deletion, we have the array memory used anyway
        if self.size > 0:
            self.size -= 1
        
        return self.arr[self.size]

    def resize(self) -> None:
        '''when at capacity, double the capacity
        and then copy elements in the new array
        '''
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        # copy elements to new_arr
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity