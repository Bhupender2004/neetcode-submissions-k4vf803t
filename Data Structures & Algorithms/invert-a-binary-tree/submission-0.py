# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Base case: if root is None, return None
        if not root:
            return None
        
        # Swap left and right child
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the root node
        return root

# Helper function to print the tree in level order
from collections import deque
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Example usage:
# Creating the binary tree [1,2,3,4,5,6,7]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
inverted_root = solution.invertTree(root)

# Print the output
print(level_order_traversal(inverted_root))  # Output: [1,3,2,7,6,5,4]
