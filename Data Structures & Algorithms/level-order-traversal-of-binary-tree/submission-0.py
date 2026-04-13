# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs - intiatlize queue / deque
        # loop through length of the queue
        # add to each level [] array
        # check if a node has a val before adding to the array
        # check if level array is not None, before adding to final "res" array
        res = []
        q = collections.deque()
        # we need to insert the root as the first elment in the queue
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res