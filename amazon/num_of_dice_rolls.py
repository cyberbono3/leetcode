class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        d = 2
        f= 6
        target = 7
        
        
        def helper(d, f, target):
        
        
        
        
        
        
        """
        def helper(d, target, memo):
            if (d, target) in memo:
                return memo[(d, target)]
            elif target < 0:
                 memo[(d, target)] = 0
            elif not d:
                memo[(d, target)] = int(target == 0)
            else:
                memo[(d, target)] = sum(helper(d-1, target - face, memo) for face in xrange(1, f+1))
                
            return memo[(d, target)]%(10**9+7)

        memo = {}
        return helper(d, target, memo)