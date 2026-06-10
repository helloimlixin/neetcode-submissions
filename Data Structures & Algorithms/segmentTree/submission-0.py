class Node:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    """worst case, a linear scan, O(n).
    with  segment tree, update O(log n), queryRange(L, R)
    takes O(log n) time

    indices     0   1   2   3   4   5
    nums        5   3   7   1   4   2

    each node represents an index range using the endpoints
        range [l:r] -> node (l,r)

    two operations of segment tree
        - update(index, val)
        - queryRange(l, r)
    m = (l + 2) // 2 = 2
                    (0,5)
                /           \
            (0,2)         (m+1,r)
            /       \           /       \
        (0,1)       (1,1)     (3,3) ...
        /
        (0,0)
    
    as the base case, we compute the sums for the endpoints, note
    that it's different from a heap as its not a full tree, but it
    can be implemented using array heaps
    """
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    # O(n).
    def build(self, nums, L, R):
        if L == R:
            # base case, compute sum of essentially one number (itself)
            return Node(nums[L], L, R)
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum

        return root
    
    # O(log n)
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)
    
    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.sum = val
            return
        
        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum
    

    # O(log n)
    def query(self, L: int, R: int) -> int:
        return self.range_query(self.root, L, R)
    
    
    def range_query(self, root, L, R):
        if L <= root.L and root.R <= R:
            return root.sum
        
        if R < root.L or L > root.R:
            return 0
        
        return self.range_query(root.left, L, R) + self.range_query(root.right, L, R)





