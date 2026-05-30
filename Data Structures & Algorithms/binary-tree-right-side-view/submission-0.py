# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs - for each node, add L, R children to the queue
        # repeat while popfront of queue
        # always add the back element to the res after each "level"
            # so each level is finished once 
            # to find num nodes in a levle - just take len of the queue
        res = []
        if not root:
            return res
    
        q = deque()
        q.append(root)
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                if i == level_length - 1: #rightmost node
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        

        return res
        
            


        