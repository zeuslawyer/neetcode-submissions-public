from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegreesOf, downstreamOf = {}, {}
        
        for i in range(numCourses):
            downstreamOf[i] = []
            indegreesOf[i] = 0
        
        for course, prereq in prerequisites:
            downstreamOf[prereq].append(course)
            indegreesOf[course] += 1
        
        # BFS
        q = deque()
        for course in indegreesOf:
            count = indegreesOf[course]
            if count == 0:
                q.append((course, count))

        sequence = []
        while q:
            crs, count = q.popleft()
            sequence.append(crs)
            
            for c in downstreamOf[crs]:
                indegreesOf[c] -= 1
                if indegreesOf[c] == 0:
                    q.append((c, indegreesOf[c]))

        return sequence if len(sequence)== numCourses else []

