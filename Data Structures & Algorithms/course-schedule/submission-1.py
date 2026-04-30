class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> 1 -> 2 no cycle
        # 0 -> 1 -> 2 -> 0 --- cycle, return false


        # dfs

        # loop through every "node"
        # visitSet - if node is already in visited, that means we have a loop -> return false

        visitSet = set()
        preMap = defaultdict(list)

        # init map
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

   


