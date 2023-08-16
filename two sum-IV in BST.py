class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root: TreeNode, k: int) -> bool:
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    nums = inorder(root)
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    
    return False

# Create a binary search tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# Define the target sum
k = 9

# Check if there exist two elements with sum equal to k
result = findTarget(root, k)

# Print the result
print(result)
