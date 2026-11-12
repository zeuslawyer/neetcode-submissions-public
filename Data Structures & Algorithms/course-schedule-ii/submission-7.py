from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqOf = { i:[] for i in range(numCourses)}
        indegreesOf = { i:0 for i in range(numCourses)}
        downstreamOf = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqOf[course].append( prereq )
            downstreamOf[prereq].append(course)
            indegreesOf[course] += 1

        q = deque()
        for course in range(numCourses):
            if indegreesOf[course]==0: q.append(course)

        
        ordering = []
        while q:
            crs = q.pop()

            # this course is done so append it.
            ordering.append(crs)

            for c in downstreamOf[crs]:
                # reduce the downstream courses indegree because the parent is done
                indegreesOf[c] -= 1
                if indegreesOf[c]==0:
                    q.append(c)
        
        return ordering if len(ordering) == numCourses else []
    





