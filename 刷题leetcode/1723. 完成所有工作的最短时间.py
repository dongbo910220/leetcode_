class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        l, r = max(jobs), sum(jobs)
        jobs.sort(reverse=True)

        def canDo(limit):
            buckets = [0] * k
            if backtrace(buckets, limit, 0):
                return True
            else:
                return False

        def backtrace(buckets, limit, idx):
            if idx == len(jobs):
                return True
            job = jobs[idx]
            for i in range(len(buckets)):
                if buckets[i] + job <= limit:
                    buckets[i] += job
                    if backtrace(buckets, limit, idx + 1):
                        return True
                    buckets[i] -= job
                    if buckets[i] == 0:
                        break
            return False

        while l < r:
            mid = (l + r) // 2
            if not canDo(mid):
                l = mid + 1
            else:
                r = mid
        return l