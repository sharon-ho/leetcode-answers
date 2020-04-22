## https://leetcode.com/problems/maximum-number-of-balloons/

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        instances = [text.count("b"), text.count("a"), text.count("l") / 2, text.count("o") / 2, text.count("n")]

        instances_no = int(min(instances))

        if (instances[0] >= instances_no and instances[1] >= instances_no and instances[2] >= instances_no and
                instances[3] >= instances_no and instances[4] >= instances_no):
            return instances_no
        else:
            return 0
