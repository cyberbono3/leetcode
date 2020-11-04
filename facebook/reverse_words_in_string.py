
import re

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = re.findall(r'\w+', s)
        words.reverse()
        return " ".join(words)