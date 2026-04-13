class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # push to min heap - top is min element
        # if size > k, pop smallest element


        # [2,3,1,5,4], k = 2
        # [1 2 3 4 5]

        # 5 4 <-- is our kth largest element

        # VIP club analogy - 100 people, only allow the 3 tallest people in at the very end
        # the 3rd tallest is the shortest out of those ppl, e..g. the "top " of the min heap

        my_heap = []
        heapq.heapify(my_heap)

        for num in nums:
            heapq.heappush(my_heap, num)
            if len(my_heap) > k:
                heapq.heappop(my_heap)
        
        kth_largest = heapq.heappop(my_heap)
        return kth_largest
