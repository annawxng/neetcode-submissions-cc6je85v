class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b] -- b is prereq of a, 
        # easiest build [b, a], where b is prereq of a

        # 0 to numCourses - 1
        preMap = defaultdict(list)

        # topological sort - add filtering for cycle
        for crs, prereq in prerequisites:
            # src.append(dst)
            preMap[prereq].append(crs)
        
        visit = set()
        path = set()

        for i in range(0, numCourses):
            if not self.dfs(i, preMap, visit, path):
                return False
        
        return True

    
    def dfs(self, src, preMap, visit, path):
        if src in path: # this check needs to be first
            return False
        if src in visit:
            return True
        visit.add(src)
        path.add(src)

        for neighbor in preMap[src]:
            if not self.dfs(neighbor, preMap, visit, path):
                return False
        
        path.remove(src)
        return True

        


        
