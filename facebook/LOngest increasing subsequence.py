class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        n = len(nums)
        lis = [1] * n
        
        
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i] and lis[i] - lis[j] < 1:
                    lis[i] += 1
        return max(lis)
        