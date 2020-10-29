class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(index, curr, s):
            if len(curr) == 4:
                if index == len(s):
                    res.append(".".join(curr))
                return
           
            for i in range(index, len(s)):
                w = "".join(s[index:i+1])
                if w[0] == "0" and len(w) > 1:
                    continue
                if int(w) < 0 or int(w) > 255:
                    continue
                backtrack(i+1, curr + [w], s)
             
          
            
        res = []
        backtrack(0,[],s)
        return res
        
                