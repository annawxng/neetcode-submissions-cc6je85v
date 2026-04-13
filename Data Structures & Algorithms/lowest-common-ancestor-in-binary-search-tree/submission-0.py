# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we want ot look for where the "split" occurs, where p and q are split off into left & right
        # p < lowest ancestor < q
        # if both greater than curr node, look right subtree
        # if both less than curr node, look left subtree
        # if one is in right subtree, and one is in left subtree, curr node is lowest ancestor (or the "split")
        # what if p or q is equal to root node? (or curr node) ==> thats the lowest ancestor

        # dfs / recursion
        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            # look left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else: # this covers the following:
              # if root is p
              # if root is q
              # if p and q are "split" -> also return root
            return root 



