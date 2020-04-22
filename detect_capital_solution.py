## https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        letters = list(word)

        for i in range(0, len(letters)):
            if letters[i].isupper():
                if i == 0:
                    continue
                if letters[i - 1].isupper() and (i + 1 < len(letters)) and not (letters[i + 1].isupper()):
                    return False
                if letters[i - 1].isupper():
                    continue
                else:
                    return False

        return True