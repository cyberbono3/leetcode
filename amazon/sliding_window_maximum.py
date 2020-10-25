
"""

239. Sliding Window Maximum
Hard

4290

191

Add to List

Share
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length


"""



from collections import deque
class Solution:
    def compute_max_sliding_window(self, nums, k):
        # maintain the highest element at the most level posiiton at deque
        q = deque ()
        res = []
        for i,x in enumerate(nums):
            # if we see element is bigger than rightmost element at deque, we pop eleemt from the right
            while q and nums[q[-1]]  <= x:
                q.pop()
                
            # we add index of current element in deque 
            q.append(i)
            
            # make sire the max element in queue is within sliding window
            if i - q[0]  >= k:
                q.popleft()
            
            # add the q[0] the max element  to res
            if i + 1 >= k:
                res.append(nums[q[0]])
        return res
        
sol = Solution()
print(sol.compute_max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])
             
            
            
        
        