class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if not self.stack:
            return None
        
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Create a binary search tree
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Initialize the BSTIterator
bst_iterator = BSTIterator(root)

# Perform operations and store the outputs
operations = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
outputs = []

for op in operations:
    if op == "BSTIterator":
        bst_iterator = BSTIterator(root)
        outputs.append(None)
    elif op == "next":
        outputs.append(bst_iterator.next())
    elif op == "hasNext":
        outputs.append(bst_iterator.hasNext())

# Print the outputs
print(outputs)
