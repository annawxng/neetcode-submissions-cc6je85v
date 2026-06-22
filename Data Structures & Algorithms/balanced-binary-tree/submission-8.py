# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # check if abs(leftHeight - rightHeight) > 1
        if abs(self.calcHeight(root.left) - self.calcHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def calcHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.calcHeight(root.left), self.calcHeight(root.right))
        