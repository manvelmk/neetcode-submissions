class Solution:
    def maxArea(self, heights: List[int]) -> int:
        retVal = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            leftVal = heights[left]
            rightVal = heights[right]
            distance = right - left
            
            volume = min(leftVal, rightVal) * distance
            retVal = max(retVal, volume)
            
            if leftVal < rightVal:
                left += 1
            else: # logic for both equality and leftVal > rightVal
                right -= 1
            
        return retVal