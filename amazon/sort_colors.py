class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        
        brtforce insetion sort O()
        
        red, white, blue  = 0,1,2
        
        0     1      2
        red, white, blue  = 0, 0, len(nums)-1
        
        
        while white <= blue:
            if nums[white] == 0:
                swap red and white
                increment white and red
            elif nums[white] == 1:
                white += 1
            else:
                # if nums[white] == 2
                # swap with blue
                nums[white], nums[blue] = nums[blue], nums[white]
                blue  -=1
                
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # use quicksort
        
        if not nums or len(nums)== 1: return
        
        start = 0
        end = len(nums) - 1
        index = 0
        
        # we are non the right boundaries
        while index <= end and start < end:
        # use startv to keep track of putting zeroes on the front
        # we gonig nuybmer by number in thsi array
            if nums[index] == 0:
                nums[index] = nums[start]
                nums[start] = 0
                start += 1
                index += 1
            elif nums[index]  == 2:
                nums[index]  = nums[end]
                nums[end] = 2
                end -= 1
            # if it is one we move our index forward
            else :
                index += 1
                