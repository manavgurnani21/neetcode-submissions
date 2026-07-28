class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum_nums = numbers[l] + numbers[r]
            if sum_nums == target:
                return [l + 1, r + 1]
            elif sum_nums < target:
                l += 1
            else:
                r -= 1
        