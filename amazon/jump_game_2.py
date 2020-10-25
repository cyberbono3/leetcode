class Solution(object):
    def jump(self, nums):
        
        # greedy approach
        last_jump_index, max_coverage, jumps = 0,0,0
        i = 0
        n = len(nums)
        while i < n - 1:
            max_coverage = max(max_coverage, i + nums[i])
            
            if i == last_jump_index:
                jumps += 1
                
                last_jump_index = max_coverage
                
                if last_jump_index >= n -1:
                    return jumps
        return jumps
            
        