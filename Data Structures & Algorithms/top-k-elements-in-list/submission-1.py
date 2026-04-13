class Solution:
    # make freq dict first
    # then loop through dict and make min_heap

    # 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        min_heap = []
        for num in nums:
            counts[num] += 1
        # 4:1, 1:1, -1:2, 2:2, 3:1
        for number, freq in counts.items():
            heapq.heappush(min_heap, (freq, number))
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        res = []
        for freq, number in min_heap:
            res.append(number)
        return res

