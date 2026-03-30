# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the tree is empty, return 0
        if not root:
            return 0
        
        # Recursively calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return the maximum depth plus 1 (for the current node)
        return max(left_depth, right_depth) + 1

# Example usage:
# Creating the binary tree [1,2,3,null,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

solution = Solution()
depth = solution.maxDepth(root)

# Print the output
print("Output:", depth)  # Output: 3
