'''
https://leetcode.com/problems/knight-probability-in-chessboard/
'''
memo = {(20, 30):1, (22, 305):12}
for (i, j), prob in memo.items():
    print(i, j, prob)


# import collections
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        memo, out_board_p = {(r, c): 1}, 0
        for step in range(K):
            next_memo = collections.defaultdict(int)
            for (i, j), prob in memo.items():
                for di, dj in moves:
                    next_i, next_j = i + di, j + dj
                    if 0 <= next_i < N and 0 <= next_j < N:
                        next_memo[(next_i, next_j)] += prob * 0.125
                    else:
                        out_board_p += prob * 0.125
            memo = next_memo
        return 1 - out_board_p

'''
Success
Details 
Runtime: 112 ms, faster than 98.20% of Python online submissions for Knight Probability in Chessboard.
Memory Usage: 12.9 MB, less than 58.56% of Python online submissions for Knight Probability in Chessboard.
'''

