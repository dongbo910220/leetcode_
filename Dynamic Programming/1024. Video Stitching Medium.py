'''
https://leetcode.com/problems/video-stitching/

Success
Details
Runtime: 332 ms, faster than 6.52% of Python online submissions for Video Stitching.
Memory Usage: 13.5 MB, less than 52.17% of Python online submissions for Video Stitching.
'''

class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        if T == 0:
            return 0
        Inf = 101
        dp = [[101] * 101 for _ in range(101)]
        for clip in clips:
            clip_s = clip[0]
            clip_e = clip[1]
            for length in range(1, T+1):
                for i in range(0, T - length + 1):
                    j = i + length
                    if clip_s > j or clip_e < i: continue
                    elif clip_s <= i and clip_e >= j: dp[i][j] = 1
                    elif clip_s <= i and clip_e < j:
                        dp[i][j] = min(dp[i][j], dp[clip_e][j] + 1)
                    elif clip_s > i and clip_e >= j:
                        dp[i][j] = min(dp[i][j], dp[i][clip_s] + 1)
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][clip_s] + 1 + dp[clip_e][j])
        return dp[0][T] if dp[0][T] != Inf else -1