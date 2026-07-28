class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        curr_min = nums[l]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                curr_min = min(curr_min, nums[mid])
                l = mid + 1
            else:
                curr_min = min(curr_min, nums[mid])
                r = mid - 1
        
        return curr_min