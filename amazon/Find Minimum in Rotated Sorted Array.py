class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        
        
        fidn a povit point
        nums = [3,4,5,1,2]
                    l
                  m
                  r
        
        
        
        while left <= ri
        
        
        
        
        """
        
        def find_pivot(left, right):
            while left <= right:
                mid = left + (right - left)// 2
                if mid +1 < n and nums[mid+1] < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            return left
        
        def binary_search(left, right):
            
                
                
        n = len(nums)
        pivot = find_pivot(0, n-1)
    
    
        min1 = binary_search(0, pivot )
        min2 = binary_search(pivot+1, n-1)
        
        return min(min1,min2)
                