class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen_par(curr, opened, closed):
            if not opened and not closed:
                res.append(curr)
                return 0
            open_par = gen_par(curr + "(", opened-1, closed) if opened else 0
            closed_par = gen_par(curr + ")", opened, closed-1) if opened < closed else 0
            return open_par + closed_par
        res = []
        gen_par("", n, n)
        return res
        