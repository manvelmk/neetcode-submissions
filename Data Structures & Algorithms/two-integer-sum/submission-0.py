class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        touched = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in touched:
                return [touched[diff], i]
            else:
                touched[num] = i