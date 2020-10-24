class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        
        
                                    8
        Input: S = "a b a b c b a c a  defegdehijhklij"
        Output: [9,7,8]
        
        
        dic = {c:i for (i,c) in enumerate(S)}
        
        left = 0
        right = 0
        
        
        right = max(right, dic[c])
        
        
        
        i = 0  
        right = 9
        
        if i == right:
            res.append(right - left +1)
            left = i+ 1
        
        
        
        
        
        """
        
        dic = {c:i for i,c in enumerate(S)}
        right, left = 0, 0
        res = []
        for i,c in enumerate(S):
            right = max(right, dic[c])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res
        