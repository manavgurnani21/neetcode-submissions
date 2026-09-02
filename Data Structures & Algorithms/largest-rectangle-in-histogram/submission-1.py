class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        max_area = area

        height_stack = []

        for r in range(len(heights)):
            while len(height_stack) > 0 and heights[r] < heights[height_stack[-1]]:
                right_wall = r
                current = height_stack.pop()
                left_wall = -1 if len(height_stack) < 1 else height_stack[-1]
                area = (right_wall - left_wall - 1) * heights[current]
                max_area = max(max_area, area)
            height_stack.append(r)

        right_wall = len(heights)

        while len(height_stack) > 0:
            current = height_stack.pop()
            left_wall = -1 if len(height_stack) < 1 else height_stack[-1]
            area = (right_wall - left_wall - 1) * heights[current]
            max_area = max(max_area, area)
        
        return max_area
