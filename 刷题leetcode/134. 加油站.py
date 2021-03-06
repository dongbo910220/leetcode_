class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        start = 0
        remain = 0
        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]
        return start