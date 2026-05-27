# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterate through each tree recursively, return false if any node is diff
        if not p:
            if q:
                return False
            return True
        if not q:
            if p:
                return False
            return True
        if p.val != q.val:
            return False
        # check both left and right subtrees

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        