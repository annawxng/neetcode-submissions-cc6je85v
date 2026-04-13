class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        min_heap = []
        for num in nums:
            counts[num] += 1
        for number, freq in counts.items():
            heapq.heappush(min_heap, (freq, number))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = []
        for freq, number in min_heap:
            res.append(number)
        return res

