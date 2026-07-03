class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visitSet, preMap (adj list), dfs through every course
        # return False if not dfs() for any of them
        # remove crs from visitSet and preMap at end of dfs functio
        # if preMap[crs] is empty, it has no prereqs so it can be completed --> return True



        visitSet = set()
        preMap = { i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = [] # don't remove just set to empty
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


