

from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        
        
        brtutforce 
            iterate over permutations
                take a max ostring of them
        
        3, 30  we want 330 instead 303
        
        
        """
        def comparator(x,y):
            if x + y > y + x:
                return -1
            elif y + x > x +y:
                return 1
            else:
                return 0
            
            
        str_nums = [str(x) for x in nums]
        str_nums.sort(key = cmp_to_key(comparator))
        return "".join(str_nums).lstrip("0") or '0'
            
            
        
            
            
        
        