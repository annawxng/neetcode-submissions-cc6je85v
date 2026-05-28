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
        _, isBalanced = self.calcHeight(root)
        return isBalanced
        


    def calcHeight(self, root: Optional[TreeNode]) -> tuple[int, bool]:
        isBalanced = True
        if not root:
            return [0, True]

        # check if it's balanced
        leftHeight, leftBalanced = self.calcHeight(root.left)
        rightHeight, rightBalanced = self.calcHeight(root.right)

        isBalanced = (leftBalanced and rightBalanced) and abs(leftHeight - rightHeight) <= 1
        return [1 + max(leftHeight, rightHeight), isBalanced]


        