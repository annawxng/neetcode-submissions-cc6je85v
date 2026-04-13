class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use min heap?
        # push all the elements into min heap
        # pop top of min heap, keep going until its not consecutive number and keep track of "longest_seq"

        if not nums:
            return 0
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
        
        longest = 1
        curr_seq = 1
        min = heapq.heappop(min_heap)
        # longest = 1
        # curr_seq = 3
        # nums=[0,3,2,5,4,6,1,1]
        # min_heap=[3, 4,5,6]
        # min = 2
        # curr_min = 3
        while min_heap:
            curr_min = heapq.heappop(min_heap)
            if (curr_min - min) == 1:
                curr_seq += 1
            elif (curr_min == min):
                continue
            else:
                longest = max(longest, curr_seq)
                curr_seq = 1
            min = curr_min
        return max(longest, curr_seq)

        