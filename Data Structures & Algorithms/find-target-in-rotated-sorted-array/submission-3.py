class Solution:
    def search(self, nums: List[int], target: int) -> int:
        retVal = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            midpoint = (left + right) // 2

            if target == nums[midpoint]:
                return midpoint
            elif target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            elif nums[left] <= nums[midpoint]:
                if ((target < nums[left])
                    or (target > nums[midpoint])):
                    left = midpoint + 1
                else:
                    right = midpoint - 1
            else:
                if ((target > nums[right])
                    or (target < nums[midpoint])):
                    right = midpoint - 1
                else:
                    left = midpoint + 1

        return retVal