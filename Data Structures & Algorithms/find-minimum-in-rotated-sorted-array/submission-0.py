class Solution:
    def findMin(self, nums: List[int]) -> int:
        retVal = nums[0]
        numRange = len(nums) - 1
        left = 0
        right = numRange

        while left <= right:
            if nums[left] < nums[right]:
                retVal = min(retVal, nums[left])
                break
            
            middleIndex = (left + right) // 2 # integer division, no decimal index lol
            retVal = min(retVal, nums[middleIndex])

            if nums[middleIndex] >= nums[left]:
                # move to the right half
                left = middleIndex + 1
            else:
                right = middleIndex - 1

        return retVal