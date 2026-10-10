class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        retVal = 0
        left = 0
        charOccur = {} # holds each unique character's occurances

        for right, char in enumerate(s):
            currentCount = charOccur.get(char, 0)
            charOccur[char] = currentCount + 1
            
            distance = right - left + 1
            if distance - max(charOccur.values()) > k:
                # reduce the count for the leftmost character
                # since it's no longer part of the window
                charOccur[s[left]] -= 1
                # shift window right if we overshot k
                left += 1
                
            # Note, cannot rely on distance value here needs to account
            # for potential left pointer shift above
            retVal = max(retVal, right - left + 1)
            
        return retVal