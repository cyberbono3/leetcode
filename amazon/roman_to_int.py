class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        wescan string
          if next character is greater then current we substract current from res
            else:
                we add current ot res
        Dont forget to add the last character.
        
        Input: "III"
        Output: 3
        
        Input: "I  V
                -1+5
                
        Input: "I   X"
                -1  10
        
        
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s)-1):
            curr, next = s[i], s[i+1]
            if dic[curr] < dic[next]:
                res -= dic[curr]
            else:
                res +=  dic[curr]
        return res + dic[s[-1]]
            