class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        
        candidates = [2,3,6,7], target = 7
                      ^
        curr_sum = 6   cur = [2,2,2]
        
        
        
        
        
        def compute_combinations(index,curr_sum, curr):
                      
            for i in range(index, len(candidates)):
                if curr_sum + nums[i] > target:
                    continue
                compute_combinations(i, curr_sum + nums[i], curr + [nums[i]])
                compute_combinations(i+1, curr_sum, curr)
                
        
        
        """
        def compute_combinations(index, curr_sum, curr):
            if curr_sum == target:
                res.add(tuple(curr))
                return
                      
            for i in range(index, len(candidates)):
                if curr_sum + candidates[i] > target:
                    continue
                compute_combinations(i, curr_sum + candidates[i], curr + [candidates[i]])
                compute_combinations(i+1, curr_sum + candidates[i], curr +[candidates[i]])
        
        res = set()
        compute_combinations(0,0, [])
        return res