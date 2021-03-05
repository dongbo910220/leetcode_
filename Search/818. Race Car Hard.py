'''
https://leetcode.com/problems/race-car/submissions/

Success
Details
Runtime: 1020 ms, faster than 33.60% of Python online submissions for Race Car.
Memory Usage: 47 MB, less than 32.52% of Python online submissions for Race Car.
'''


class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = collections.deque()
        queue.append((0, 1, 0))
        seen = set([(0, 1)])

        while queue:
            position, speed, step = queue.popleft()
            if position == target:
                return step
            if position < 0 or position > 10001:
                continue
            for instruction in "AR":
                if instruction == 'A':
                    position1 = position + speed
                    speed1 = speed * 2
                    step1 = step + 1
                    if (position1, speed1) not in seen:
                        seen.add((position1, speed1))
                        queue.append((position1, speed1, step1))
                else:
                    # position keep
                    position2 = position
                    if speed <= 0:
                        speed2 = 1
                    else:
                        speed2 = -1
                    step2 = step + 1
                    if (position2, speed2) not in seen:
                        seen.add((position2, speed2))
                        queue.append((position2, speed2, step2))


a = Solution()
a.racecar(4)