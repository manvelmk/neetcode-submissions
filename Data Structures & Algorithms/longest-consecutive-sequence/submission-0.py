class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        retVal = 0
        hashSet = set(nums)
        
        for number in nums:
            if (number - 1) not in hashSet:
                length = 0 # always clear out the length
                while (number + length) in hashSet: # iterate one at a time and build up the length
                    length = length + 1
                retVal = max(retVal, length) 
        return retVal