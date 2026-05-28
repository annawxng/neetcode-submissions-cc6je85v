# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        if not root:
            return 0
        self.calcHeight(root)
        self.calcHeight(root.left)
        self.calcHeight(root.right)
        return self.max_diameter

    def calcHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.calcHeight(root.left)
        rightHeight = self.calcHeight(root.right)
        self.max_diameter = max(leftHeight + rightHeight, self.max_diameter)
        return 1 + max(leftHeight, rightHeight)
