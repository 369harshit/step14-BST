class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.firstStartPoint = None
        self.lastEndPoint = None
        self.prevNode = None
        
        def findSegments(root):
            if not root:
                return
            
            findSegments(root.left)
            
            if self.prevNode:
                if self.prevNode.val > root.val:
                    if not self.firstStartPoint:
                        self.firstStartPoint = self.prevNode
                    self.lastEndPoint = root
            self.prevNode = root
            
            findSegments(root.right)
        
        findSegments(root)
        x = self.firstStartPoint.val
        self.firstStartPoint.val = self.lastEndPoint.val
        self.lastEndPoint.val = x
    
    def printInOrder(self, root):
        if not root:
            return
        
        self.printInOrder(root.left)
        print(root.val)
        self.printInOrder(root.right)

# Create the initial tree
root = TreeNode(10)
n1 = TreeNode(15)
n2 = TreeNode(5)
n3 = TreeNode(4)
n4 = TreeNode(7)
n5 = TreeNode(14)
n6 = TreeNode(17)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n2.left = n5
n2.right = n6

solution = Solution()

print("In-Order traversal of BST before recovery:")
solution.printInOrder(root)

solution.recoverTree(root)

print("In-Order traversal of BST after recovery:")
solution.printInOrder(root)
