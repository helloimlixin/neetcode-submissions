class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def hash_function(self, key):
        return  key % self.capacity
    
    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)

        curr = self.table[index]

        if not curr:
            self.table[index] = ListNode(key, value)
        else:
            prev = None
            while curr:
                if curr.key == key:
                    curr.value = value # size not increment here by returning
                    return
                prev, curr = curr, curr.next
            prev.next = ListNode(key, value)
        
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        curr = self.table[index]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        curr = self.table[index]
        prev = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[index] = curr.next # only one node at bucket
                self.size -= 1
                return True
            prev, curr = curr, curr.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                index = node.key % self.capacity
                if not new_table[index]:
                    new_table[index] = ListNode(node.key, node.value)
                else:
                    head = new_table[index]
                    node.next = head
                    new_table[index] = node # order doesnt really matter
                node = node.next
        
        self.table = new_table


