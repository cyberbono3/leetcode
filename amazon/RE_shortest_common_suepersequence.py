from functools import lru_cache

class Solution:
    def shortestCommonSupersequence(self, s, t):
        @lru_cache(50000)
        def dp(s, t):
            if s == "": return t
            if t == "": return s
            if s[-1] == t[-1]:
                return dp(s[:-1], t[:-1]) + s[-1]
            else:
                return min(dp(s[:-1], t) + s[-1], dp(s, t[:-1]) + t[-1], key=len)
        return dp(s, t)