## https://leetcode.com/problems/positions-of-large-groups/

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        intervals = []
        i = 0
        j = 0

        for j in range(0, len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    intervals.append([i, j])
                i = j + 1

        return intervals
