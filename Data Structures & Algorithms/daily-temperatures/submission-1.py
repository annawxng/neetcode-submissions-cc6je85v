class Solution:
    # 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack of pair [temp, idx]
        res = [0]*len(temperatures) # note: cannot initialize this to empty
                                # specifiy the len so u can directly index into it
        stack = []
        for i, t in enumerate(temperatures):
            # check while stack is not empty
            while stack and t > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                res[stack_idx] = (i - stack_idx)
            stack.append([t, i])  # make sure this line is outside of the while loop
        return res
