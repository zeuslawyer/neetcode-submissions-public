from collections import deque

# Kahns Algo with BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        downstreamOf, indegreesOf = {}, {}

        for i in range(numCourses):
            downstreamOf[i] = []
            indegreesOf[i] = 0
        
        for crs, pre in prerequisites:
            downstreamOf[pre].append(crs)
            indegreesOf[crs] += 1
        
        
        q = deque()
        for course in range(numCourses):
            if indegreesOf[course] == 0:
                q.append(course)
        
        done = 0
        while q:
            c = q.popleft()
            done += 1
            
            for ds in downstreamOf[c]:
                indegreesOf[ds] -= 1
                if indegreesOf[ds] == 0:
                    q.append(ds)

        return done == numCourses