'''
https://leetcode.com/problems/smallest-sufficient-team/

Success
Details
Runtime: 196 ms, faster than 89.36% of Python online submissions for Smallest Sufficient Team.
Memory Usage: 19.8 MB, less than 87.23% of Python online submissions for Smallest Sufficient Team.
'''


class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        dp = {0: []}

        skill_to_index_map = {
            skill: index for index, skill in enumerate(req_skills)
        }

        for index in range(len(people)):
            person_skills_bit_req = 0
            for skill in people[index]:
                person_skills_bit_req |= (1 << skill_to_index_map[skill])
            tasks = list(dp.keys())

            for task_i in tasks:
                new_task = (task_i | person_skills_bit_req)
                if (new_task not in dp) or (len(dp[new_task]) > len(dp[task_i]) + 1):
                    dp[new_task] = dp[task_i] + [index]
        return dp[(1 << len(req_skills)) - 1]

dp  = {'aa': [2, 3],
       'bb' : [2, 6]}
for person in dp.keys():
    print(person)