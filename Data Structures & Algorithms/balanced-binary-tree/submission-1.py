# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recurse through the tree
        # calc height of left subtree
        # calc height of right subtree -- once that height exceeds diff of 1, return false
            # brute force - dont check for diff as u go, just check the total height diff
            # optimal - when calculating the height of right subtree, check if abs is > 1
                # along the way
        # else return true
        if not root:
            return True
        if abs(self.calcHeight(root.left) - self.calcHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def calcHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.calcHeight(root.left), self.calcHeight(root.right))


        