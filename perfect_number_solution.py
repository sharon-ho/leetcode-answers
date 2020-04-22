## https://leetcode.com/problems/perfect-number/

import math

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        sum = 0

        if num <= 0:
            return False

        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum += i
                if i * i != num:
                    sum += num / i

        if sum - num == num:
            return True
        else:
            return False