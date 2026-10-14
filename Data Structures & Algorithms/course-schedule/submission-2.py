class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
          # STEP 1: build two lookups from the input.
        # Each pair is [course, prereq]: you must take prereq BEFORE course.

        # prereqsOf[course] = list of prereqs (upstream) that course needs
        upstreamOf = {}
        # dependents[prereq] = list of courses that are downstream of this prereq
        downstreamOf = {}

        for course in range(numCourses):
            upstreamOf[course] = []
            downstreamOf[course] = []

        for course, prereq in prerequisites:
            upstreamOf[course].append(prereq)
            downstreamOf[prereq].append(course)

        # STEP 2: for each course, count how many prereqs are still unfinished.
        # At the start, that's all of them.
        indegrees = [] 
        for course in range(numCourses):
            indegrees.append(len(upstreamOf[course]))

        # STEP 3: courses with 0 prereqs can be taken right now.
        # Put them in the queue.
        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        # STEP 4: take courses one at a time.
        courses_taken = 0

        while q:
            course_done = q.popleft()
            courses_taken += 1

            # Finishing this course decrements the indegrees for downstream courses
            for downstream_course in downstreamOf[course_done]:
                indegrees[downstream_course] -= 1   # one fewer unfinished prereq

                # If that was its last unfinished prereq, it's now takeable.
                if indegrees[downstream_course] == 0:
                    q.append(downstream_course)

        # STEP 5: did we take every course?
        # If there's a cycle (A needs B, B needs A), those courses never hit 0
        # remaining, never enter the queue, and courses_taken falls short.
        return courses_taken == numCourses
        