class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
    
       dic = {}
       
       iterate over point i from 0 to n-2 (including)
          interate over point i+1 to n-1 (including)
           first_point, second_point = points[i], points[j]
            slope = (second_point[1] - first_point[1]) /  (second_poiunts[0] - first_point[0] )
            if slope in dic:
                dic[slope] += 1
            else:
                dic[slope] = 2
                
          return max(dic.values())
              
        [[1,1],[2,2],[3,3]
        
        
       
        
        """
        dic = {}
        
        n = len(points)
        
        max_points = 0
        
        for i in range(n-1):
            dic = {}
            same = 0
            for j in range(i+1, n):
                first_point, second_point = points[i], points[j]
                dx,dy = second_point[1] - first_point[1], second_point[0] - first_point[0]
                if not dx and not dy:
                    same += 1
                    continue
                if not dy:
                    continue
                slope = dx/dy * 1.0
                if slope in dic:
                    dic[slope] += 1
                else:
                    dic[slope] = 2
            max_points = max(max_points, max(dic.values())  +same )
        return max_points
                