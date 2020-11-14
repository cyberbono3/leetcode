
import re

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
           
        str = re.findall('^[+\-]?\d+', str.strip())

        try:
            res = int(''.join(str))
            MAX = 2147483647
            MIN = -2147483648
            if res > MAX:
                return MAX
            if res < MIN: 
                return MIN
            return res
        except: 
            return 0
        
        