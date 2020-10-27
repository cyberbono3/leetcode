class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        eight = [1,8,6,2,5,4,8,3,7]
                 0 1 2 3 4 5 6 7 8
        
        
        """
      
            
        
    
        left, right = 0, len(height)-1
        max_area = 0
        h, w = 0, 0
        while left < right:
            w = right - left
            if height[left] == height[right]:
                h = height[left]
                left += 1
                right -= 1
            elif height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            max_area = max(max_area , h*w)
        return max_area
            
                