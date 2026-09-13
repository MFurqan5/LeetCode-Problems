class Solution(object):
    def minMirrorPairDistance(self, nums):
        def rev(x):
            r = 0
            while x > 0:
                r = r * 10 + x % 10
                x //= 10
            return r
        
        seen = {}
        ans = float('inf')
        
        for j, num in enumerate(nums):
            if num in seen:
                ans = min(ans, j - seen[num])
            seen[rev(num)] = j
        
        return ans if ans != float('inf') else -1