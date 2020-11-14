from heapq import heappush, heappop
from collections import Counter

class Solution(object):
    def reorganizeString(self, S):
        c = Counter(S)
        
        h = []
        
        
        res = ""
        max_freq = c.most_common()[0][1]
        
        #  max_freq + (max_freq-1) <= len(S)
        if 2*max_freq -1 > len(S):
            return res
            
        
        for char, count in c.items():
            heappush(h, (-count, char))
            
        
        while len(h) >= 2:
            _, char1 = heappop(h)
            _, char2 = heappop(h)
            
            if c[char1] :
                c[char1] -= 1
                res += char1
                heappush(h, (-c[char1], char1))
            
            if c[char2] :
                c[char2] -= 1
                res += char2
                heappush(h, (-c[char2], char2))
      
        
        return res
            
                