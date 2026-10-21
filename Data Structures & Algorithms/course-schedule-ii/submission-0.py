from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sequence = []
        indegreesOf = defaultdict(int)
        downstreamOf = defaultdict(list)

        for course, prereq in prerequisites:
            downstreamOf[prereq].append(course)
            indegreesOf[course] += 1 

        # BFS
        q = deque()
        for course in range(numCourses):
            if indegreesOf[course] == 0:
                q.append(course)
        
        while q:
            current = q.popleft()
            sequence.append(current)

            for ds in downstreamOf[current]:
                indegreesOf[ds] -= 1
                if indegreesOf[ds] == 0:
                    q.append(ds)
                
        return sequence if len(sequence) == numCourses else []


