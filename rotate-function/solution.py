class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        
        f = sum(i * nums[i] for i in range(n))
        best = f
        
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            if f > best:
                best = f
        
        return best