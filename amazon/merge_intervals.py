class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        sort by begin
        
        add first itnerval to output
        
        startign from first inteervals
             if begin is greater then end of the last output intrrval
                    there is no overlap
                    add the current interval to output andcontinue
             there is an overlap
             start_intervla = min(current_begin, and the last output begin )
             end_itnerval = max(currentintervlaend , lastoutput_ened)
             pop the last itnerval from output and add the modfiied one
        
        
        
        """
        if not intervals:
            return None
        if len(intervals) == 1:
            return intervals
        
        
        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > output[-1][1]:
                output.append(intervals[i])
                continue
        
            start = min(intervals[i][0], output[-1][0])
            end = max(intervals[i][1], output[-1][1])
            output.pop()
            output.append([start, end])
        return output