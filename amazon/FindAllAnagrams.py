

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        
        abc = [cba, bca]
            0123
        s = abab    p = ab 
            
        c1 = Counter(p)
        outout = [0,1,2]
        [ab]
        [ba]
        [ab] 
        
        
        s: "cbaebabacd" p: "abc"
        
        [cba]
        
        c1 = counter(p)  $ O(len(p)
        for scan the string:  O(n-k+1)
            c2 = Counter(s[i:i+l])  O(l)
            c = c1.subtract(c2) 
            if all(not v for v in c.values()):
                result.append(i)
                
            
        
        
        
        
        l = len(p)
        p = "".join(sorted(p))
        for i inrange(n-l+1):  O(n-l+1)
            w = "".join(sorted(s[i:i+l]))  O(llogl)
            if w == p:
                result.append(i)
            
    
        TC O( (n - l +1)  * llogl ))
        
        
        
        res = []
        n = len(s)
        l = len(p)
        
        sorted_p = "".join(sorted(p))
        
        
        for i in range(n-l+1): 
            w = "".join(sorted(s[i:i+l]))  
            if w == sorted_p:
                res.append(i)
        return res
            
            0 1 2 3 4 5 6 7 8 9
        s: "c b a e b a b a c d" p: "abc"
                        ^   
                            ^
        
        dic =  e:1, b:1, a:1
        
        result = [0,]
        
        
        def increment_and delete(start):
        
        
        c = Counter(p)
        
        dic = Counter()
        
        start = 0
        for i in range(n-l+1):
            
            dic[s[i]] += 1

            if i - start +1 >= len(p):
                if c == dic:
                    res.append(start)
                start += 1
                if dic[s[start]]  == 1:
                    del dic[s[i]]
                else:
                    dic[[s[start]]] -= 1
            
          
                
                
                
                
        
        
        
        
        
        """
          
        c1 = Counter(p)
        
        c2 = Counter()
        
        n = len(s)
        
        l = len(p)
        
        res = []
        start = 0
        for i in range(n):
            
            c2[s[i]] += 1

            if i - start +1 >= l:
                if c1 == c2: # O(l)
                    res.append(start)
                if c2[s[start]] == 1:
                    del c2[s[start]]
                else:
                    c2[s[start]] -= 1
                start += 1
        return res
        