from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # upstreamOf = defaultdict(list)
        downstreamOf = defaultdict(list)
        indegreesOf = defaultdict(int)

        for course, prereq in prerequisites:
            # upstreamOf[course].append(prereq)
            downstreamOf[prereq].append(course)
            indegreesOf[course]+=1

        q = deque()
        for course in range(numCourses):
            if indegreesOf[course] == 0:
                q.append(course)

        completed = 0
        while q:
            current = q.popleft()
            completed += 1

            for ds in downstreamOf[current]:
                indegreesOf[ds] -= 1
                if indegreesOf[ds] == 0:
                    q.append(ds)
        
        return completed == numCourses
