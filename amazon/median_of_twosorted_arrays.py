class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        pick a pivit point every element at left side is less than every element on the right side
        
    
        
        1. equal number of elements should be at the each side 
        x x x x | x x  lLong rLong
          y | y y y    lShort rShort
          
         if we can fidn this pivot point than the median will be within 4 numbers
         
        2.
         after picking a pivot point , it's possible to determine whether to go left or right
         
          1 2 4 | 5 6 8  if 4 > 3 then we can move the pointer to lethe left 
          2   3 6 | 7       if 6 greater tan 5 we move pointer to the left othwerwise
                  if 3 less 5and 4 lesss 4 
                  
          strategy to pick every possible pviot point in smaller array, find corresponding pivot point in a larger array chec kfi it's correct if not move either pivot point in a smaller array or pivotpoint at the larger array
          
         3. code outline:
            1. binary search at small array
            2. getIndices m - > lLong, rLong
            3. getDirection: lLong, rLong -> get direction ( left or right)
            4. make sure indices are correct lLong rLong, lShort rShort calculate them median
                median = average(max(lLOng,lShort), min(rShort, lLong) ))
        
        """
        # return 4 incdices
        def getIndices(rShort):
            longMid =  (m + n )// 2
            rLong = longMid - rShort
            return (rShort-1, rShort, rLong-1, rLong)
        def getDirection(lShort, rShort, lLong, rLong):
            
            if shortArr[lShort] < longArr[rLong] and longArr[lLong] < shortArr[rShort]:
                return 0
            elif shortArr[lShort] > longArr[rLong] or longArr[lLong]  > shortArr[rLong]
               return  1
            elif 
               
                
            
            
        #determien long and short arrays
        m, n = len(nums1), len(nums2)
        shortArr, longArr = nums2, nums1
        if m < n:
            shortArr, longArr = nums1, nums2
        left, right = 0, len(shortArr)-1
        while d != 0: # i wil lreplace it in a second
            mid = left + (right - left) // 2
            lShort, rShort, lLong, rLong = getIndices(mid)
            d = getDirection(lLong, rLong)
            if d < 0 :  # we go to left 
                r = mid -1
            elif d > 0:
                # go the right
                l = mid +1
         
        
        # direction is found
         # compute median 