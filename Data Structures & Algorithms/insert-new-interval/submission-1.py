class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        isInserted = False
        # don't modify the original cur, just modify newInterval
            # and then insert it when there are no more intervals to merge

        # cases:
        # case 1: new comes before cur, insert new
        # case 2: cur comes before new
        # case 3: can be merged - merge into new, don't append yet
        for i in range(len(intervals)):
            cur = intervals[i]
            if newInterval[1] < cur[0]:
                if not isInserted:
                    res.append(newInterval)
                    isInserted = True
                res.append(cur)
            elif cur[1] < newInterval[0]:
                res.append(cur)
            # merge together since they overlap
            else:
                newInterval[1] = max(newInterval[1], cur[1])
                newInterval[0] = min(newInterval[0], cur[0])
        if not isInserted:
            res.append(newInterval)

        return res
            

            

# intervals = [[1,3],[4,6]], newInterval = [2,5]
# Output: [[1,2],[3,5],[9,10]]   new: [6,7]
