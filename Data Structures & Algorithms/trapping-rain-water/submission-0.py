class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        left_heights = [0] * len(height)
        max_height = 0
        for i in range(1, len(height)):
            left_heights[i] = max(height[i - 1], max_height)
            max_height = max(max_height, height[i - 1])
        
        right_heights = [0] * len(height)
        max_height = 0
        for i in range(len(height)-2, -1, -1):
            right_heights[i] = max(height[i + 1], max_height)
            max_height = max(max_height, height[i + 1])
        
        area_collected = 0
        
        for i in range(1, len(height)-1):
            delta_left = max(left_heights[i]-height[i],0)
            delta_right = max(right_heights[i]-height[i],0)
            area_collected += min(delta_left, delta_right)
        
        return area_collected
            

