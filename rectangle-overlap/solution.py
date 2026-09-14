class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1_1, y1_1, x2_1, y2_1 = rec1
        x1_2, y1_2, x2_2, y2_2 = rec2
        
        if x2_1 <= x1_2 or x2_2 <= x1_1:
            return False
        if y2_1 <= y1_2 or y2_2 <= y1_1:
            return False
        
        return True