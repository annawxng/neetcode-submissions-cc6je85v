class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # given integer n
        # n courses -> 1 to n
        # relations -- relations[i] = [prevCourse, nextCourse]
        # prevCourse is preReq to nextCourse

        # one semester - take any number of courses
            # need all prereqs in the previous semester for the courses you are taking
        
        # return minimum number of semesters needed to take all courses
        # return -1 if not possible


        # Examples

        # 1st sem - Course 1 and 2, 
        # Second sem - take course 3
        
        # Cycle -> return -1

        # detect a cycle - have a visit set
            # --> if you've seen the number before / in set --> return -1
        
        # keep track of # semesters -> increment for each time a course has a prereq
            # (but don't add for multiple prereqs for the same course)

        
        # preMap  [crs] -> [pre1, pre2], defaultdict(list)

        # when looping through relations - i[0] is the prereq, i[1] is the crs
            # store in premap as preMap[i[1]].append(i[0])
            # if it's not in map, increment numSem by 1
        
        # return numSem


        # edge case

        # 1 -> 3
        # 2 -> 3
        # 4 -> 2
        # 5 -> 1
        # sem 1 - take 4 and 5 // how do we determine this as a new sem
        # sem 2 - take 1 and 2
        # sem 3 - take 3

        # when course has no prereq - you can add one to the sem, but also, it has to be
        # a "diff" level, e.g. 4 and 5 both do not have prereqs but they can be taken in one sem
        
        # ok yea idk how to do topological sort at all

        
        
        # how many prereqs [crs] has
        # oh so prereq_count[3], means count for course 3, but we would have it indexed by count[3]
        # so if we have course == 3 == n, we need 4 spots bc if we do [0] * 3, that would only be index 0-2
        # 0th index is not used but we need to allocate it
    
        prereq_count = [0] * (n + 1)
        # courses unlocked by completing "course" -- "course" is prereq of [crs1, crs2, etc]
        next_courses = defaultdict(list)
        sem_q = deque()
        # instead of visited, at end, check if numCourses != n, then return -1
        # 
        preMap = defaultdict(list)
        # next_courses: 1 : 3, 2:3
        # prereq_count: [0, 0, 0, 2]

        for prev, next in relations:
            next_courses[prev].append(next)
            prereq_count[next] += 1
        
        # oh this is counting the sentinel 0
        for idx, count in enumerate(prereq_count):
            if count == 0 and idx != 0:
                sem_q.append(idx) # here idx is the course
       
        numSem = 0
        numCourses = 0

        while sem_q:
            sem_size = len(sem_q)
            for _ in range(sem_size):
                curr = sem_q.popleft()
                print("curr: ", curr)
                numCourses += 1
                for crs in next_courses[curr]:
                    prereq_count[crs] -= 1
                    print("crs: ", crs)
                    print("pre count: ", prereq_count[crs])
                    if prereq_count[crs] == 0:
                        sem_q.append(crs)
                print("numCourses: ", numCourses)
                
            numSem += 1
        print("numCourses: ", numCourses)
        if numCourses != n:
            return -1
        return numSem





        
        


