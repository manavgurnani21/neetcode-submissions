class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first create a hash table for easy indexing
        numsTable = dict()
        # iterate through each number
        for i in range(len(nums)):
            complement = target - nums[i] # calculate the complement for the number
            # if the complement exists within the hashtable
            if complement in numsTable:
                return [numsTable[complement], i]  # return [complementIndex, currIndex]
            numsTable[nums[i]] = i # store index of number in hash-table
