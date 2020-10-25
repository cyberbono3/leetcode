from heapq import heappush, heappop
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        
        
        Input: [[0, 30],[5, 10],[15, 20]]
        
        https://leetcode.com/problems/meeting-rooms-ii/
        
    
        """
        
        intervals.sort(key = lambda x:x[0])
        
        h = []
        
        for b,e in intervals:  #O(n)
            # there is no overlap we pop from the heap
            if h and b >= h[0]:
                heappop(h) #O(log k)
            # we add curent to the heap   
            heappush(h, e)  #Log k
        
        # Overall time complexity is O(n log k)
        return len(h)
    
sol = Solution()
print(sol.minMeetingRooms([[0, 30],[5, 10],[15, 20]]) == 2)