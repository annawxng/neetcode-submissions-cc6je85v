# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # return lowest common ancestor between two nodes
        # if q is child of p, return p, 
        # if p is child of q, return q
        # p = 1, q = 8, lowest would be 5
        # p = 2, q = 4, lowest would be 3
        # if p and q are both children of same parent, then the parent is the ancestor

        # note: bst, use the vals to compare

        # p.val < root, q.val > root
            # return root
        # p.val < root and q.val < root
        # both smaller, look left
        # p.val > root and q.val > root
        # both bigger, look right
        if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val or p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            