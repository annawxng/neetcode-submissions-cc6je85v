"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = []
        ends = []

        count = 0
        max_count = 0
        s = 0
        e = 0 
        

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()

        
        n = len(starts)
        while s < n:
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            max_count = max(max_count, count)

        return max_count

        # 0 -------------------------- 40
        # 5 -- 10 15 --20

        # starts: 0, 5, s15
        # ends: 10, 20, e40

        # while [s] < [e], ++count
        # once not the case, reset count to 1
        # continue until the end



    

    # Input: intervals = [(0,40),(5,10),(15,20)]
    # Output: 2
