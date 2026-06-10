class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        
        curr = self.root

        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                # insert with replacement if matched
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        curr = self.findMin(self.root)
        
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root

        while curr and curr.right:
            curr = curr.right
        
        return curr.val if curr else -1
    
    def findMin(self, node):
        while node and node.left:
            node = node.left
        
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self, curr, key) -> TreeNode:
        # note that it's easier to set a non trivial
        # return type as we will be augmenting the tree
        # while doing removal, the method will not only
        # remove the node with key, but also return the
        # new root of the tree

        # base case
        if not curr:
            return None
        
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                # tricky case, swap the curr with the inorder
                # successor (node with the smallest key in the
                # right subtree)
                min_node = self.findMin(curr.right) # guaranteed no left child
                curr.key = min_node.key
                curr.val = min_node.val

                # delete the min_node
                curr.right = self.removeHelper(curr.right, min_node.key)
        
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []

        self.inorderHelper(self.root, result)

        return result

    def inorderHelper(self, root, result):
        if not root:
            return
        
        self.inorderHelper(root.left, result)
        result.append(root.key)
        self.inorderHelper(root.right, result)
