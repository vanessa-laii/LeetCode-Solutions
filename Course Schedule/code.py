class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build an adjacency list
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)

        # add all with indegree 0 or no dependencies to a queue
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)

        finish = 0
        while queue:
            # complete this course
            course = queue.popleft()
            finish += 1

            for n in adj[course]:
                # number of dependecies this has minus 1
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        return finish == numCourses