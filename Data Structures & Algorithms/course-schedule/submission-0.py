from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # STEP 1: build two lookups from the input.
        # Each pair is [course, prereq]: you must take prereq BEFORE course.

        # prereqsOf[course] = list of prereqs that course needs
        prereqsOf = {}
        # dependents[prereq] = list of courses that are waiting on this prereq
        dependents = {}

        for course in range(numCourses):
            prereqsOf[course] = []
            dependents[course] = []

        for course, prereq in prerequisites:
            prereqsOf[course].append(prereq)
            dependents[prereq].append(course)

        # STEP 2: for each course, count how many prereqs are still unfinished.
        # At the start, that's all of them.
        remaining = []
        for course in range(numCourses):
            remaining.append(len(prereqsOf[course]))

        # STEP 3: courses with 0 prereqs can be taken right now.
        # Put them in the queue.
        q = deque()
        for course in range(numCourses):
            if remaining[course] == 0:
                q.append(course)

        # STEP 4: take courses one at a time.
        courses_taken = 0

        while q:
            course_done = q.popleft()
            courses_taken += 1

            # Finishing this course helps every course waiting on it.
            for waiting_course in dependents[course_done]:
                remaining[waiting_course] -= 1   # one fewer unfinished prereq

                # If that was its last unfinished prereq, it's now takeable.
                if remaining[waiting_course] == 0:
                    q.append(waiting_course)

        # STEP 5: did we take every course?
        # If there's a cycle (A needs B, B needs A), those courses never hit 0
        # remaining, never enter the queue, and courses_taken falls short.
        return courses_taken == numCourses