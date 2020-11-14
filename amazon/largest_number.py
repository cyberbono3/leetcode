

from itertools import permutations

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        
        
        brtutforce 
            iterate over permutations
                take a max ostring of them
        
        
        
        """
        largest = ""
        for p in permutations(nums, len(nums)):
            s = "".join([str(x) for x in p])
            largest = max(largest, s)
        return largest
            
            