from collections import defaultdict

class Solution:
    ALPHABET_COUNT = 26 #lowercase only, strs[i] is made up of lowercase English letters.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retVal = defaultdict(list)

        for word in strs:
            count = [0] * Solution.ALPHABET_COUNT
            
            for char in word:
                count[ord(char) - ord("a")] += 1 #one way to get the "index" of a character
            
            retVal[tuple(count)].append(word)

        return list(retVal.values())