class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs_left(target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if target <= nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            return left
        
        def bs_right(target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            return right
        
        
        if not nums:
            return [-1,-1]
        
        if len(nums)  == 1:
            return [0,0] if nums[0] == target else [-1,-1]
        
        
            
        left_index, right_index = bs_left(target),bs_right(target)
        return [left_index, right_index] if left_index <= right_index else [-1,-1]
                
        