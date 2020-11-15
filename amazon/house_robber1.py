class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd_sum, even_sum = 0, 0
        
        for i,x in enumerate(nums):
            if i % 2:
                odd_sum = max(odd_sum +x , even_sum)
            else:
                even_sum = max(even_sum +x , odd_sum)
        return max(odd_sum, even_sum)