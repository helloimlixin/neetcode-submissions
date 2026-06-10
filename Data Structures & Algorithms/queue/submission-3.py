class Node:
    '''A doubly linked list node.
    '''
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.pre = None

class Deque:
    
    def __init__(self):
        # two dummy nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def isEmpty(self) -> bool:
        return self.head.nxt == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.pre

        last_node.nxt = new_node
        new_node.pre = last_node
        new_node.nxt = self.tail
        self.tail.pre = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.nxt

        self.head.nxt = new_node
        new_node.pre = self.head
        new_node.nxt = first_node
        first_node.pre = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        target_node = self.tail.pre # essentially the last node
        val = target_node.val
        prev_node = target_node.pre

        prev_node.nxt = self.tail
        self.tail.pre = prev_node

        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        target_node = self.head.nxt # essentially the first node
        val = target_node.val
        next_node = target_node.nxt

        self.head.nxt = next_node
        next_node.pre = self.head

        return val
