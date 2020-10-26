from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        
        linear approach
        
        l = lenT
        icnrement l = 4
        
        
        while l:
        
            ABC all present in BANC
            s = set(T)

            we scan the string s:
               w = [BANC]  O(l)
               if s.subset(set(w))  O(le(s)):
                return w

            O( (n-l+1 ) *  n * (l + len(s)))  = O(n**2)
            return ""
    
         window_size = len(t)
        
        s = set(t)
        
        n = len(s)
        
        
        
        while window_size < n: 
            for i in range(n - window_size + 1):
                w_list = s[i:i+window_size]
                print(w_list)
                if s.issubset(set(w_list)):
                    return "".join(w_list)
            window_size += 1
        return ""
                
        bruteforce
        
        S = "ADOBECODEBANC", T = "ABC"
        
        
    
    
        
        
        """
        c = Counter(t)
        
        window_dic = defaultdict(int)
        
        required = len(t)
        formed = 0
        
        res = (float("inf"), 0, 0)
        
        l,r =  0, 0
        
        while r < len(s):
           
            window_dic[s[r]] += 1
            if s[r] in c:
                formed += 1
            while l < r and formed == required:
                window = r - l + 1
                if window < res[0]:
                    res = (window, l, r)
                if s[l] in c and window_dic[s[l]] <= c[s[l]]:
                    formed -= 1
                window_dic[s[l]] -= 1
                l += 1
        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]