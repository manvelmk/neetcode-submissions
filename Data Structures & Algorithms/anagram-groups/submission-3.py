from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        retVal = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            retVal[key].append(word)
        return list(retVal.values())