class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        # build adj for all courses 
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        result = []
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            result.append(course)
            for dependentCourse in adj[course]:
                indegree[dependentCourse] -= 1
                if indegree[dependentCourse] == 0:
                    queue.append(dependentCourse)
        
        return result if len(result) == numCourses else []

        