# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # needs to match subroot exactly, if there's extra left / right child, it won't work
        # iterate through root, if val is same as the subroot, then iterate and check if the subroot exists,
            # then u can return true or false based on that
            # edge case - if both trees are the same it's true
        # check null cases
        if not root:
            if subRoot:
                return False
            return True
        if not subRoot:
            if root:
                return False
            return True

        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
            
        
        if not root:
            return False
        # there exists root where val is same as subRoot, check if sameTree
        return isSameTree(root, subRoot)

    # call this function when the root val is same as subRoot val
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # basically the funciton i defined earlier

        # check null cases
        if not p:
            if q:
                return False
            return True
        if not q:
            if p:
                return False
            return True

        # check values are not the same
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)