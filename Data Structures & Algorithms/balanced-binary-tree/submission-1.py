# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_balance(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            
            return height, balanced
        
        _, is_balanced = check_balance(root)
        return is_balanced

# Helper function to build a binary tree from a list
def build_tree(values):
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    
    return root

# Example usage:
# Example 1
root1 = build_tree([3, 9, 20, None, None, 15, 7])
solution = Solution()
print(solution.isBalanced(root1))  # Output: True

# Example 2
root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
print(solution.isBalanced(root2))  # Output: False

# Example 3
root3 = build_tree([])
print(solution.isBalanced(root3))  # Output: True
