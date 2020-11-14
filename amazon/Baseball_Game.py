class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        
        n = len(ops)
        i = 0
        while i < n:
            if ops[i].isnumeric():
                stack.append(int(ops[i]))
            elif ops[i] == "C":
                stack.pop()
            elif ops[i]  == "D":
                stack.append(stack[-1]*2)
            elif ops[i] == '+':
                stack.append(stack[-1] + stack[-2])
            i += 1
        return sum(stack)