class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        depth = 0
        result = []
        
        for c in seq:
            if c == '(':
                result.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                result.append(depth % 2)
        
        return result