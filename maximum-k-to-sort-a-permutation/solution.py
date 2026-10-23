class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = -1
        
        # The maximum k is the bitwise AND of all elements that are currently out of place.
        # If an element is already at its correct index (nums[i] == i), it doesn't need to be moved.
        # For all mismatched elements, their bitwise AND will tell us the maximum common 'k' that allows them to be swapped.
        
        for i in range(n):
            if nums[i] != i:
                if ans == -1:
                    ans = nums[i]
                else:
                    ans &= nums[i]
        
        # If the array is already sorted, return 0.
        return max(0, ans)