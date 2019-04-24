class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [[0] * numCourses for _ in range(numCourses)]
        indegree = [0] * numCourses

        for i in range(len(prerequisites)):
            ready = prerequisites[i][0]
            pre = prerequisites[i][1]
            if matrix[pre][ready] == 0:
                indegree[ready] += 1
            matrix[pre][ready] = 1

        count = 0
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            course = queue.pop(0)
            count += 1
            for i in range(numCourses):
                if matrix[course][i] != 0:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)

        return count == numCourses
