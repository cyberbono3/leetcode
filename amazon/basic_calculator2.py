"""

227. Basic Calculator II
Medium

1704

292

Add to List

Share
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

https://leetcode.com/problems/basic-calculator-ii/


"""


class Solution:
    def calculate(self, s):
        
        num = 0
        pre_op = '+'
        s+='+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif not c.isspace():
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop()*num)
                elif pre_op == '/':
                    stack.append(stack.pop()//num)
                num = 0
                pre_op = c
        return sum(stack)
        
sol = Solution()
print(sol.calculate(" 3+5 / 2 "))

            
            