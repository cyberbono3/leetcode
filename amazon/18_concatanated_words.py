"""


472. Concatenated Words
Hard

906

121

Add to List

Share
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.





"""








class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        
       "catsdogcats"
       
      
        c atsdogcats
        
        case 1 cats dogcats
        
         case 2  dog cats
       
       
       
       
       
      
       
      
             
             
             
        
        """
        def dfs(word):
            if not word:
                return True
            
            for i in range(1,len(word)):
                prefix = word[:i]
                suff = word[i:]
              
            
                if prefix in words_set and suff and suff in words_set:
                    return True
                
                
                if prefix in words_set and dfs(suff):
                    return True
                
    
            return False
                
            
            
            
        
        words_set = set(words)
        return [w for w in words if dfs(w)]
  
      