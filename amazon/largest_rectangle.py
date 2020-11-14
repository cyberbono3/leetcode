class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        max_area = 0
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            bars = []
            for j in range(n):
                bar = 0
                for i in range(row, m):
                    h = int(matrix[i][j])
                    if h == 0:
                        break
                    else:
                        bar += 1
                bars.append(bar)
            max_area = max(max_area, self.largestRectangleArea(bars))
        return max_area

    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        i = 0
        while i <= len(heights):
            h = heights[i] if i < len(heights) else 0
            if not stack or h >= heights[stack[-1]]:
                stack.append(i)
            else:
                top = stack.pop()
                dist = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, dist * heights[top])
                i -= 1
            i += 1
        return max_area
        