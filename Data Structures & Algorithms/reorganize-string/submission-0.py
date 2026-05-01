class Solution:
    def reorganizeString(self, s: str) -> str:
        # a: -3
        # b: -1
        # c: -1

        # edge case: 
        # a: -2
        # b: -1
        # c: -1

        #res = a


        # edge case: 
        # a: -2
        # b: 0
        # c: 0
        # a b a c a

        # 
        # a: 0
        # b: 0
        # c: 0
        # a b a c a


        counts = Counter(s)
        maxHeap = []
        for char, count in counts.items(): #i keep forgetting items() for dict
            maxHeap.append([-count, char]) # we want to negate count to create maxHeap
            # Note - to "decrement" our count we have to += or increment since it's negative
        
        heapq.heapify(maxHeap) # make sure to heapify outside the while loop
        res = ""
        
        prev = None
        while maxHeap or prev:
            # we want or prev since we want to check edge case for when prev exists but MaxHeap doesnt
            if prev and not maxHeap:
                return "" # let me try to visualize this better later

            count, max_char = heapq.heappop(maxHeap)
            res += max_char
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = [count, max_char] # we dont want to set as prev if the count becomes 0
        return res

