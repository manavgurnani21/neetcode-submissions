# Notes:
# Need to design system to check for duplicates
# Need to keep count of each value that appears
# BF: arrays to keep count for each type of value
# Optimized: hash tables to keep count of each value, mark as true if count already > 0
from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values_seen_dict = defaultdict(int)

        for num in nums:
            if(values_seen_dict[str(num)] > 0):
                return True
            values_seen_dict[str(num)] += 1

        return False