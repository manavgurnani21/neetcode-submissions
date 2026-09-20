class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Optimized approach: Boyer-Moore generalized
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        # Phase 1: find candidates
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: verify
        result = []
        for c in (candidate1, candidate2):
            if nums.count(c) > len(nums) // 3:
                result.append(c)
        return result