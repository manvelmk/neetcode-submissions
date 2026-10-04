# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        retVal = []
        frequency = {}
        # size of list's elements and each element holds a list of reoccurring numbers of that element's index times
        heatmap = [[] for size in range(len(nums) + 1)] 
        
        # Step 1: go through the given list and build the number frequency counter
        for number in nums:
            frequency[number] = frequency.get(number, 0) + 1
        
        # Step 2: populate a "heatmap" of occurences (buckets of frequency)
        for number, count in frequency.items():
            heatmap[count].append(number)
            
        # Step 3: reverse loop through the heatmap so that the most occurrances are considered first
        for i in range(len(heatmap) - 1, 0, -1):
            for val in heatmap[i]: # loop through each sublist if any and record the values if any
                retVal.append(val)
                if len(retVal) >= k: # up to our desired max number
                    return retVal
                
        return retVal