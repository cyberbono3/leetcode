class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        0 ^ 3 = 3
        3 ^ 0 = 3
        3 ^ 1
        """
        res = len(nums)
        for i, v in enumerate(nums):
            res ^= i
            res ^= v
        return res
        