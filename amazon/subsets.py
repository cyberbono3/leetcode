class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
               [1,2,3]
              /        \
            [1],[2,3]   [], [2,3]
             /       \
         [1,2],[3]  [1], [3]
        
        
        
        """
        def generate_subsets(index, curr):
            if index == len(nums):
                res.add(tuple(curr))
                return
            generate_subsets(index+1, curr + [nums[index]])
            generate_subsets(index+1, curr )
            
            
            
                
        res = set()
        generate_subsets(0, [])
        return list(res)
            