class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # always default to smallHeap by default
        heapq.heappush(self.small, -1 * num) # need to mulitply by -1 since python is default minHeap, and we want maxHeap for smallHeap

        # make sure every number in small <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # some value in smallheap is larger than largeheap
            # pop from small and add to largeheap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size
        if len(self.small) > len(self.large) + 1: # difference of 1 is ok
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # do the same yhing but we are popping from largeheap instead
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val) # need to multiply by -1 whenever we add and pop from smallHeap
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # return largest value in small
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        
        #  else, even number
        median = float(self.small[0] * -1 + self.large[0]) / 2
        return median
        
        