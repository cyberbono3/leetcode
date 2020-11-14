class Solution(object):
    def minDistance(self, word1, word2):
        """
        
        
        Insert a character
        Delete a character
        Replace a character
        Example 1:
        
        
        
        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation: 
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
        
        
        
        
        """
        def helper(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            elif i == len(word1):
                memo[(i, j)] = len(word2) - j
            elif j == len(word2):
                memo[(i, j)] = len(word1) - i    
            elif word1[i] == word2[j]:
                # just increment the both pointers
                 memo[(i, j)] = helper(i+1, j+1, memo)
            else:
                # min of replacement ,insertion and deletion 
                replace = helper(i+1, j+1, memo)
                insert = helper(i, j+1, memo)
                delete = helper(i+1, j, memo)         
                memo[(i, j)] = 1 + min(replace, insert, delete)
            return memo[(i, j)] 
        return helper(0,0, {})
        