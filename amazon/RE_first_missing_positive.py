# https://leetcode.com/problems/first-missing-positive/

# https://emre.me/coding-patterns/cyclic-sort/


class Solution:
    def missingNumber(self, nums):
      
      
      
      class Solution(object):
        def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        #razobratjsja
        
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):
            if nums[i]/n==0:
                return i
        return n
        

