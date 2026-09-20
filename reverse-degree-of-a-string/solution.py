class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, c in enumerate(s):
            reversed_pos = 26 - (ord(c) - ord('a'))
            total += reversed_pos * (i + 1)
        return total