class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0   # minimum possible open count
        high = 0  # maximum possible open count
        
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low = max(low - 1, 0)
                high -= 1
                if high < 0:
                    return False
            else:  # '*'
                low = max(low - 1, 0)
                high += 1
        
        return low == 0