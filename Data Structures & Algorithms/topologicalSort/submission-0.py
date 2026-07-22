class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adj list [A, B]
        adj = {}
        for i in range(0, n):
            adj[i] = []
        for src, dst in edges: # [A, B]
            adj[src].append(dst)

        topSort = []
        visit = set()
        path = set()
        # go through list of nodes
        # i: label of node
        # run dfs on it, 
        # after we run dfs on each node, we have topSort, and we want to reverse it
        for i in range(0, n):
            if not self.dfs(i, adj, visit, path, topSort):
                return []
        topSort.reverse()
        return topSort
    # src = current node
    # adj = adj list --> we want to go thru all neighbors
    # visit - has it alr been visited? --> return

    def dfs(self, src, adj, visit, path, topSort):
        if src in path:
            return False # cycle
        if src in visit:
            return True
        
        visit.add(src)
        path.add(src)

        for neighbor in adj[src]:
            if not self.dfs(neighbor, adj, visit, path, topSort):
                return False
        topSort.append(src)
        path.remove(src)
        return True
        