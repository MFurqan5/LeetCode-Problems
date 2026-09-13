class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        
        from collections import Counter
        shifts = Counter()
        
        for i1, j1 in ones1:
            for i2, j2 in ones2:
                shifts[(i1 - i2, j1 - j2)] += 1
        
        return max(shifts.values()) if shifts else 0