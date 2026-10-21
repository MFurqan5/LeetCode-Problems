class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[-1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        
        # prefix_sum[i] stores the number of reachable indices from 0 to i-1
        prefix_sum = [0] * (n + 1)
        
        for i in range(1, n):
            # Update prefix sum for the previous index
            prefix_sum[i] = prefix_sum[i - 1] + (1 if dp[i - 1] else 0)
            
            if s[i] == '0':
                # We can reach i from any j such that:
                # i - maxJump <= j <= i - minJump
                left = max(0, i - maxJump)
                right = i - minJump
                
                if right >= 0:
                    # Count of reachable indices in [left, right]
                    reachable_count = prefix_sum[right + 1] - prefix_sum[left]
                    if reachable_count > 0:
                        dp[i] = True
                        
        return dp[n - 1]