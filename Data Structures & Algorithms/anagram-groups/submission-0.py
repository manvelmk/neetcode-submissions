class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retVal = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            retVal[key].append(word)
        return list(retVal.values())