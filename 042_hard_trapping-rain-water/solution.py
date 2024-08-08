class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [0] * len(height)
        
        max_rights = [0] * len(height)
        
        
        for i in range(1, len(height)):
            max_lefts[i] = max(max_lefts[i-1], height[i-1])
        
        for i in range(-2, -len(height), -1):
            max_rights[i] = max(height[i+1], max_rights[i+1])
            
        ans = 0
        for i in range(1, len(height) -1):
            if min(max_lefts[i], max_rights[i]) > height[i]:
                ans += min(max_lefts[i], max_rights[i]) - height[i]
            
        return ans        
    

class Solution2:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water