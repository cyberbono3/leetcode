class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        
        [0,1,3,5,6,8,12,17]
                   
     
        
        """
        visited = set()
      
        stack = [(stones[0], 0)]
        stones_set = set(stones)
        while stack:
            stone, last_jump = stack.pop()
            if stone == stones[-1]:
                return True
            visited.add((stone, last_jump))
            for j in (last_jump - 1, last_jump, last_jump + 1):
                new_stone = stone + j
                if j > 0 and new_stone in stones_set and (new_stone, j) not in visited:
                    stack.append((new_stone, j))
        return False
                
        
     