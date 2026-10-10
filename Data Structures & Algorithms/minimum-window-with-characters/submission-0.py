class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            # short circuit the logic. Satisfies edge case
            return ""
        
        found = False
        slidingPopulation = {} # population within the sliding window
        targetPopulation = {} # maps the target strings character occurances
        left = 0
        pending = 0 # stores the running count of matched characters with their occurances
        
        result = [-1, -1] # default result is undefined
        resLen = float("infinity") # default result length, an unreachably high number

        # populate the target map from the target string
        for char in t:
            targetPopulation[char] = targetPopulation.get(char, 0) + 1

        for right, char in enumerate(s):
            # increment our window population
            slidingPopulation[char] = slidingPopulation.get(char, 0) + 1

            # making sure the current character is in the target
            # and their population counts match
            # increment the pending character occurrances matched
            if ((char in targetPopulation) and
                (slidingPopulation[char] == targetPopulation[char])):
                pending += 1
                
            # keep shrinking the window from the left side
            # while the pending count matches the target population's
            while pending == len(targetPopulation):
                range = right - left + 1
                if (range) < resLen: # initially any value of range will satisfy this
                    result = [left, right]
                    resLen = range
                    found = True
                
                # reduce the leftmost character's occurance from our sliding window
                slidingPopulation[s[left]] -= 1 
                
                # now, after reduction, the pending matches may be reduced too
                if ((s[left] in targetPopulation) and 
                        (slidingPopulation[s[left]] < targetPopulation[s[left]])):
                    pending -= 1
                # finally, slide the left pointer
                left += 1
                
        if found:
            return s[result[0]: result[1] + 1]
        else:
            # it is still possible to not have found a single result
            return ""