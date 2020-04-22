## https://leetcode.com/problems/defanging-an-ip-address/

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        defanged_address = address.replace(".", "[.]")

        return defanged_address
