
import bisect

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        bruteforce approach
        
        n = len(nums)
        
        brtuteforce TC O(n**2)
        res = []
        for i in range(n-1):
            count = 0
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
        return res
        
                0 1 2 3
        nums = [5,2,6,1]
        
       
        
        
        
        """
        s = sorted(nums)
        ans = []
        
        for x in nums:
            i = bisect.bisect_left(s, x)
            ans.append(i)
            s.pop(i)
        return ans