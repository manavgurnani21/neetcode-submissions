class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # check if left side sorted
            if nums[l] <= nums[mid]:
                # if target in left side
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1 # going left
                else:
                    l = mid + 1
            # elif check if right side sorted
            elif nums[r] >= nums[mid]:
                # if target in right side, go right
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1 # going left
                else:
                    r = mid - 1
        
        return -1

