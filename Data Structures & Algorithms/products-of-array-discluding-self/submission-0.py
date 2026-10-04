class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        
        pfx = 1
        for i, num in enumerate(nums):
            products[i] = pfx
            pfx = nums[i] * pfx
            
        pstfx = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] = products[i] * pstfx
            pstfx = nums[i] * pstfx
            
        return products