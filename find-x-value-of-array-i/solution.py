class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0] * k
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            r = num % k
            for x in range(k):
                new_dp[(x * r) % k] += dp[x]
            new_dp[r] += 1
            for x in range(k):
                res[x] += new_dp[x]
            dp = new_dp
        
        return res