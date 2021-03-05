'''
Success
Details
Runtime: 456 ms, faster than 15.73% of Python online submissions for Course Schedule.
Memory Usage: 14.1 MB, less than 57.63% of Python online submissions for Course Schedule.
'''


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = [0] * numCourses
        for course_pair in prerequisites:
            courses[course_pair[0]] += 1

        num = 0
        stack = []
        for i in range(len(courses)):
            if courses[i] == 0:
                num += 1
                stack.append(i)

        while stack:
            i = stack.pop()
            for course_pair in prerequisites:
                if course_pair[1] == i:
                    courses[course_pair[0]] -= 1
                    if courses[course_pair[0]] == 0:
                        num += 1
                        stack.append(course_pair[0])

        return num == numCourses



'''
Success
Details 
Runtime: 76 ms, faster than 93.03% of Python online submissions for Course Schedule.
Memory Usage: 14.1 MB, less than 57.63% of Python online submissions for Course Schedule.

'''

from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for i, j in prerequisites:
            edges[j].append(i)
            degree[i] += 1

        num = 0
        queue = deque([])
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
                num += 1
        # print(num)

        while queue:
            i = queue.popleft()
            for j in edges[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.append(j)
                    num += 1
        # print(num)
        # print(queue)
        return num == numCourses




