"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?



"""


from heapq import heapify, heappush, heappop


class MedianFinder:
    def __init__(self):
        self.lowers = []    # max heap
        self.uppers = []    # min heap
        heapify(self.lowers)
        heapify(self.uppers)
        
    def rebalance(self):
        if len(self.lowers) - len(self.uppers) >= 2:
            heappush(self.uppers, -heappop(self.lowers))
        elif len(self.uppers)  - len(self.lowers) >= 2:
            heappush(self.lowers, heappop(self.uppers))
            
        
    def addNum(self, num):
        if not self.lowers or num < -self.lowers[0]:
            heappush(self.lowers, -num)
        else:
            heappush(self.uppers, num) # 
            
        self.rebalance()
    

    def findMedian(self):
        # if the sizzes are equal return the median of max of lower_heap and min of upper_heap
        if len(self.lowers)  == len(self.uppers):
            return  (-self.lowers[0] + self.uppers[0]) / 2.0
        
        # lowers size is bigger than uppers
        elif len(self.lowers)  > len(self.uppers):
            return -self.lowers[0]
        
        
        # uppwer size is greater than uppers
        else:
            return  self.uppers[0]
             
            

            
            
            
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()