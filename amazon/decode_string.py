class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        
        3[a2[c]]"
        
        k_stack = ["3, "2"]
        str_stack = "a"
        curr_str = c"
        
        accaccacc
        
        """
        
        str_stack, k_stack = [] , []
        curr_num, curr_str = "", ""
        ans = ""
        
        for ch in s:
            if ch.isnumeric():
                curr_num += ch
            elif ch.isalpha():
                curr_str += ch
            elif ch == "[":
                k_stack.append(curr_num)
                curr_num = ""
                str_stack.append(curr_str)
                curr_str = ""
            elif ch == "]":
                k = int(k_stack.pop())
                curr_str *= k
                curr_str = str_stack.pop() + curr_str
            if not k_stack:
                ans += curr_str
                curr_str = ""
        return ans
                
                               
        