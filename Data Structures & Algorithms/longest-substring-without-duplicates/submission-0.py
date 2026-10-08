class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        retVal = 0
        seen_map = {}
        left = 0

        for i, char in enumerate(s) :
            if char in seen_map and seen_map[char] >= left:
                left = seen_map[char] + 1
            
            seen_map[char] = i
            retVal = max(retVal, i - left + 1)

        return retVal
