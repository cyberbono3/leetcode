class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        
           "23"
          /  |  \ 
        "a"  "b" "c"
        / \
      "af""ad""ae"
        
        
        
        """
        dic = {
            "2":"abc",
            "3":"def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "vxyz"
         }
               
        def rec(index, curr):
            if index == n:
                res.append(curr)
                return 
            for c in dic[digits[index]]:
                rec(index+1, curr + c)
                
          
        res = []
        n = len(digits)
        rec(0, "")
        return res
        