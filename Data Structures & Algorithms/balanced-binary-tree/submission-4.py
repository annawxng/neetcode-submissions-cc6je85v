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
        height, isBalanced = self.calcHeight(root)
        if isBalanced is False:
            return False
        leftHeight, isBalanced_left = self.calcHeight(root.left)
        if isBalanced_left is False:
            return False
        rightHeight, isBalanced_right = self.calcHeight(root.right)
        if isBalanced_right is False:
            return False
        return True
        


    def calcHeight(self, root: Optional[TreeNode]) -> (int, bool):
        isBalanced = True
        if not root:
            return 0, True

        # check if it's balanced
        leftHeight, leftBalanced = self.calcHeight(root.left)
        rightHeight, rightBalanced = self.calcHeight(root.right)

        if not (leftBalanced and rightBalanced):
            isBalanced = False

        if abs(leftHeight - rightHeight) > 1:
            isBalanced = False
        return (1 + max(leftHeight, rightHeight), isBalanced)


        