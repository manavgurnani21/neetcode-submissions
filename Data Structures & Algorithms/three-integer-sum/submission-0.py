class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)

        triplets = set()

        for i in range(len(nums_sorted) - 1):
            l = i + 1
            r = len(nums_sorted) - 1
            target = -nums_sorted[i]
            while l < r:
                val = nums_sorted[l] + nums_sorted[r]
                if val == target:
                    triplets.add((nums_sorted[i], nums_sorted[l], nums_sorted[r]))
                    l += 1
                elif val < target:
                    l += 1
                else:
                    r -= 1
        
        return list(triplets)