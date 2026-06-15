class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Counter
        nums_counter = Counter(nums)
        # nums = [1,2,2,3,3,3], k = 2
        # 1:1, 2:2, 3:3
        res = []
        min_heap = []
        heapq.heapify(min_heap)
        for num, freq in nums_counter.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        for freq, num in min_heap:
            res.append(num)
        return res





        