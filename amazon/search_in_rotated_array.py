class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
                       0 1 2 3 4 5 6
        Input: nums = [4,5,6,7,0,1,2], target = 0
                             
                               m
                                    r
                          
       
       """
       #binary search
       left , right = 0, len(nums) - 1
       while left <= right:
              mid = left + (right - left) // 2
              if target == nums[mid]:
                return mid
              # left side of the array is sorted
              if nums[left] <= nums[mid]:
                  if nums[left] <= target < nums[mid]:
                        right = mid -1
                   else:
                        left = mid + 1
              # right side of the array sorted
              elif num[mid] <= nums[right]:
                 if nums[mid] < target <= nums[right]:
                    left = mid +1
                 else:
                    right = mid -1
        return -1
                    