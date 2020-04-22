## https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        count = 0

        valid_types = list(J)

        my_stones = list(S)

        for s in my_stones:
            if s in valid_types:
                count += 1

        return count
