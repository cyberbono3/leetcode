"""

32. Longest Valid Parentheses
Hard

4109

149

Add to List

Share
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
Accepted





"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        
          0 1 2 3 4 5
         "),(,),(,),)"
                  ^
         
         
          s = ") ) ( ) ) ( ) ( )"
               0 1 2 3 4 5 6 7 8
         
         
         stack = []
         maxans = 2
         
         
         scan the string
         if char = "(":
            we push i tothe stack
         else:
             stack.pop()
             if not stack:
                we push(i)
             else:
                we maxnas = max(manxans, i, - stack[-1])
                
             
         s = "("
         
         s = ")"
         
         if len(s) < 2:
            return 
         
         "()"
        
        
        """
        if len(s) < 2:
            return 0
        
        
        stack = [-1]
        maxans = 0
        
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
                    
        return maxans