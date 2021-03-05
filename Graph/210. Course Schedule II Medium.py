'''
Success
Details
Runtime: 464 ms, faster than 5.19% of Python online submissions for Course Schedule II.
Memory Usage: 14.1 MB, less than 38.89% of Python online submissions for Course Schedule II.
'''


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        courses = [0] * numCourses
        for course_pair in prerequisites:
            courses[course_pair[0]] += 1

        num = 0
        stack = []
        list = []
        for i in range(len(courses)):
            if courses[i] == 0:
                num += 1
                stack.append(i)
                list.append(i)

        while stack:
            i = stack.pop()
            for idx, course_pair in enumerate(prerequisites):
                if course_pair[1] == i:
                    courses[course_pair[0]] -= 1
                    if courses[course_pair[0]] == 0:
                        num += 1
                        stack.append(course_pair[0])
                        list.append(course_pair[0])
                    # prerequisites.pop(i)

        if num == numCourses:
            return list
        else:
            return []

''' 
Success
Details 
Runtime: 76 ms, faster than 97.28% of Python online submissions for Course Schedule II.
Memory Usage: 14.2 MB, less than 38.89% of Python online submissions for Course Schedule II.
'''
from collections import deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
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
        res = []
        queue = deque([])
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
                num += 1
        # print(num)

        while queue:
            i = queue.popleft()
            res.append(i)
            for j in edges[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    queue.append(j)
                    num += 1
        # print(num)
        # print(queue)
        if num == numCourses:
            return res
        else:
            return []