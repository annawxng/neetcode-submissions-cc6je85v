class Solution:
      def leastInterval(self, tasks: List[str], n: int) -> int:
        # find the frequencies of ech ask
        counts = Counter(tasks)  # 'A':3, 'B':2, 'C':3

        maxHeap = []

        # create heap
        for task, count in counts.items():
            maxHeap.append(-count)

        heapq.heapify(maxHeap) # maxheap is now: -3,-2, -2

        q = deque()

        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap:
                # get count of maxFreq task
                count = heapq.heappop(maxHeap)
                # "decrement" then enqueue count and time available
                count += 1
                available = n + time
                if count != 0:
                    q.append([count, available])
            if q:
                #check front of the queue, pop & add back to heap when available == time
                cnt, avail = q[0]
                if avail == time:
                    q.popleft()
                    heapq.heappush(maxHeap, cnt)

        return time