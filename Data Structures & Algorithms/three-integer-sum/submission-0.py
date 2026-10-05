class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retVal = []
        sortedNums = sorted(nums)
        
        for i, num in enumerate(sortedNums):
            if i <= 0 or num != sortedNums[i - 1]: # skip diplicate reference number
                left = i + 1 # left pointer is our current index's right neighbour
                right = len(sortedNums) - 1
                while left < right:
                    leftVal = sortedNums[left]
                    rightVal = sortedNums[right]
                    sum = leftVal + rightVal + num
                    if sum > 0:
                        right -= 1
                    elif sum < 0:
                        left += 1
                    else:
                        # Found a match, add to output
                        retVal.append([leftVal, rightVal, num])
                        left += 1 # basically a do while loop
                        while left < right and sortedNums[left] == sortedNums[left - 1]:
                            left += 1
        return retVal