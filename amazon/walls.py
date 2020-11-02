class Solution:
    def find_max_val(self, n, walls):
        # edge cases 
        if not walls:
            return 0
        if len(walls)== 1:
            return walls[0]
        
        width_sum = sum(walls[i][0] for i in range(n))
    
        heights = [walls[i][1] for i in range(n)]
        
        prefix_heights, suffix_heights = [1]*n, [1]*n
        prefix_heights[0] = 0
        suffix_heights[-1]  = 0
        
        for i in range(1,n):
            prefix_heights[i] = max(prefix_heights[i-1], heights[i-1])
        
        for i in range(n-2, -1, -1):
            suffix_heights[i] = max(suffix_heights[i+1], heights[i+1])
        
        for i in range(n):
            heights[i] = max(prefix_heights[i], suffix_heights[i])
        
        res = []
        for i in range(n):
            curr_width = width_sum - walls[i][0]
            res.append(curr_width * heights[i])
        return res
            
        
            
sol = Solution()
n =3
walls = [[5,10], [4,6], [7,3]]
print(sol.find_max_val(n, walls))

        