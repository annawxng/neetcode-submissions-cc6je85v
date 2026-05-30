class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # start of second interval is <= end of first one
        # sort intervals first in ascending order of first element

        # [[1,3],[1,5],[6,7]] ==> first 2 overlap, 3rd doesnt
        # [[1,3],[1,5],[6,7], [8, 10]], [9, 13] =>  [1, 5], [6, 7], [8, 13]
        # so once we encounter a non-overlapping case, we can just push the nonoverlapping one to res
        res = []
        if not intervals:
            return res
        intervals.sort(key=lambda x : x[0])

        if len(intervals) == 1:
            res.append(intervals[0])
            return res
        start = intervals[0]
        for i in range(1, len(intervals)): # skip first element
            other_interval = intervals[i]
            if other_interval[0] <= start[1]:
                # merge the intervals
                start[1] = max(other_interval[1], start[1])
                if i == len(intervals) - 1: # last interval
                    res.append(start)
            else:
                # no overlap
                res.append(start)
                start = other_interval
                if i == len(intervals) - 1:
                    res.append(other_interval)
            

        return res




        