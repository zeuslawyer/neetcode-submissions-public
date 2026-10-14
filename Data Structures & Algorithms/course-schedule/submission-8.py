from collections import defaultdict, deque

# Kahn's algorithm - BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqsOf = defaultdict(list)
        downstreamOf = defaultdict(list)
        indegreesOf = defaultdict(int) # using dict in case courses need names.  


        for course, prereq in prerequisites:   
            prereqsOf[course].append(prereq)
            downstreamOf[prereq].append(course)
        
        #  1. count prereqs for each course
        #. 2. courses with zero prereq are starting courses 
       
        q = deque()
        # indegrees = [0] * numCourses. ---> indegrees as list works only where course labels are ints. otherwise use dict.
        for course in range(numCourses):
            indegreesOf[course] = len(prereqsOf[course])
            if indegreesOf[course] == 0:
                q.append(course)

        completed_courses = 0
        
        while q:
            currentcourse = q.popleft()

            # mark this as done
            completed_courses +=1
            # downstream courses have 1 less prereq
            for downstream in downstreamOf[currentcourse]:
                indegreesOf[downstream] -= 1

                # add to queue of downstream course now has no more upstream prereqs
                if indegreesOf[downstream] == 0:
                    q.append(downstream)
        
        return completed_courses == numCourses

            
        
        
        
        