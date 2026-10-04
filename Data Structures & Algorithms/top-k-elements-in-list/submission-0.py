class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        retVal = []
        frequency = {}
        #size of list's elements and each element holds a list of reoccurring numbers of that element's index times
        heatmap = [[] for size in range(len(nums) + 1)] 
        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1
            
        for number, count in frequency.items():
            heatmap[count].append(number)
            
        for i in range(len(heatmap) - 1, 0, -1):
            for val in heatmap[i]:
                retVal.append(val)
                if len(retVal) >= k:
                    return retVal
                
        return retVal