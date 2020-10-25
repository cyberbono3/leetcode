class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        "a b c a b c b b"
        
        longest substring without repeatign characters
        
        
        a b c a b c b b       output abc
                    ^
        
        
        max_len = 3
        s = {}
        s.add(b)
        
        we scan the string O(n)
           if char not in set:
                we add it to the set:
         else:
             max_len = max(max_len , len(s))
             s.clear()  O(l)
        add curent character to the set
        overall time comlexity O(n*l)
        TC  o(l)
    
            
    
        """
        usedChar = {}
        start = 0
        longest = 1
        
        for end in range(len(s)):
            if s[end] in usedChar and start < end:
                start = usedChar[s[end]] + 1
            else:
                longest = max(longest, end - start + 1)
            
            usedChar[s[end]] = end
        return longest
        