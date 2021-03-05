'''
https://leetcode.com/problems/keys-and-rooms/
'''
'''
Success
Details 
Runtime: 48 ms, faster than 82.12% of Python online submissions for Keys and Rooms.
Memory Usage: 13.5 MB, less than 16.67% of Python online submissions for Keys and Rooms.
'''

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = [0] * n
        # visited[0] = 1
        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                self.dfs(rooms, i, visited)
                count += 1

        return count == 1

    def dfs(self, rooms, i, visited):
        keys = rooms[i]
        for key in keys:
            if visited[key] == 0:
                visited[key] = 1
                self.dfs(rooms, key, visited)