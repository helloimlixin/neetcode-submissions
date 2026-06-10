# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        q = collections.deque()

        q.append(root)

        while q:
            qlen = len(q)
            level = []

            for _ in range(qlen):
                node = q.popleft()

                if node:
                    level.append(node.val)

                    # add children
                    q.append(node.left)
                    q.append(node.right)
            
            # discard null node's children
            if level:
                traversal.append(level)
        
        return traversal
        