class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        valid = set('0125689')
        must_change = set('2569')
        count = 0
        
        for x in range(1, n + 1):
            s = str(x)
            if all(c in valid for c in s) and any(c in must_change for c in s):
                count += 1
        
        return count