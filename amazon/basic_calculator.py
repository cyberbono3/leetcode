"""
https://leetcode.com/problems/basic-calculator/

224. Basic Calculator
Hard

1719

141

Add to List

Share
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""

class Solution:
    def calculator(self, s):
        def evaluate_expr(stack):
            res = 0 if not stack else stack.pop()
            while stack and stack[-1] != ")":
                sign = stack.pop()
                if stack and sign == '+':
                    res += stack.pop()
                elif stack and sign == "-":
                    res -= stack.pop() 
            return res
        
        n, operand, stack  = 0, 0, []
        for i in range(reversed(range(len(s)))):
            ch = s[i]
            if ch.isdigit:
                #we add operarnd in reversed order
                operand = (pow(10, n) * int(ch))  + operand
                n += 1
            elif not ch.isspace():
                if n:
                    stack.append(operand)
                    operand, n = 0, 0
                if ch == "(":
                    #14
                    res = evaluate_expr(stack)
                    stack.pop()
                    
                    stack.append(res)
                else:
                    stack.append(ch)
        if n:
            stack.append(operand)
        return evaluate_expr(stack)
            
                    
                
                
            



