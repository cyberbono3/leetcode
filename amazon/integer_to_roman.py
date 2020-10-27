class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        
        2994
        
    
    
        
        
        """
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV",
                   "I"]
        roman = ''
        
        i = 0
        while num:
            k = num // values[i]
            for _ in range(k):
                roman += symbols[i]
                num -= values[i]
            i += 1
        return roman