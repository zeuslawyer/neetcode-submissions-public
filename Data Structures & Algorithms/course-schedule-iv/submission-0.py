from collections import deque, defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        downstreamOf = defaultdict(list)
        indegreesOf = defaultdict(int) 
        prereqsOf = defaultdict(set) # stores all the prereqs of a given course

        for pre, course in prerequisites:
            downstreamOf[pre].append(course)
            indegreesOf[course]+=1

        q = deque()  
        for course in range(numCourses):
            if indegreesOf[course] == 0:
                q.append(course)
        

        while q:
            current = q.popleft()

            for course in downstreamOf[current]:
                # add the current node AND its own prereqs to its downstream's prereq set. 
                prereqsOf[course].add(current)
                prereqsOf[course].update(prereqsOf[current])
                indegreesOf[course] -= 1
                if indegreesOf[course] == 0:
                    q.append(course)
        
        res = []
        for pre, c in queries:
            if pre in prereqsOf[c]:
                res.append(True)
            else:
                res.append(False)

        return res