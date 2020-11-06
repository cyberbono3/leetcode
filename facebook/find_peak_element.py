class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        
        brutforce approacj
        
        Input: nums = [1,2,3,1]
        
        # edge cases
        
        linear time approach
        
        if n >= 3
        
        for i in range(1, n-1)
          if nums[i-1] < nums[i] > nums[i+1]:
                return i
        
        Input: nums = [1,2,1,3,5,6,4]
                                 l
                                m
                                r
                            
                            
                    
        """

        n = len(nums)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if mid +1 < n and nums[mid+1] > nums[mid]:
                left = mid +1
            else:
                right = mid-1
        return left
           
                