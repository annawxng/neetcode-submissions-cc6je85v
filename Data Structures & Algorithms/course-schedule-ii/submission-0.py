class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        
    
        Output: []
        # topological sort
        res = []

        adj = defaultdict(list)
        # build adjacency list  
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])


        # now adj list is like [A: [B, D], B:[C, E]]
        in_degrees = [0] * numCourses
        # figure out in_degrees[] for all the nodes
        for pre, courses in adj.items():
            for course in courses:
                in_degrees[course] += 1

        
        q = deque()
        for crs in range(numCourses):
            if in_degrees[crs] == 0:
                q.append(crs)

        while q:
            curr_crs = q.popleft()
            for crs in adj[curr_crs]:
                in_degrees[crs] -= 1
                if in_degrees[crs] == 0:
                    q.append(crs)
            res.append(curr_crs)
        
        if len(res) != numCourses:
            return []

        return res
        # queue - append all the nodes that have in_degree of 0

        # while queue is not empty
        #     popleft -> node
        #     loop through all neighbors of that node and decrement in_degree[neighbor] to "remove" the node
        #     if any in_degree becomes 0, append to the queue

        # time complexity O(V + E) -- visit eac node once, each edge once (V is num nodes, E is num edges)

        # check for cycle
        # if len(result) != num_nodes, its a cycle and return empty array []

