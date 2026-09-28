class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        max_depth = 0
        
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif c == ')':
                depth -= 1
        
        return max_depth