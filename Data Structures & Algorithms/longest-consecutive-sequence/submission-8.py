class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force: use sorting
        sorted_nums = sorted(nums)
        
        if len(sorted_nums) < 2:
            return len(sorted_nums)

        print(sorted_nums)
        seq_length = 0
        max_seq_length = seq_length
        for i in range(len(sorted_nums)-1):
            print(f"Comparing {sorted_nums[i]} and {sorted_nums[i + 1]}")
            if sorted_nums[i+1] == sorted_nums[i] + 1:
                print(f"Consecutive sequence found between index {i} and {i + 1}")
                seq_length += 1
                if seq_length > max_seq_length:
                    max_seq_length = seq_length
            elif sorted_nums[i+1] == sorted_nums[i]:
                print(f"Duplicate number found at {i} and {i + 1}, trying in next attempt")
                continue
            elif sorted_nums[i+1] != sorted_nums[i] + 1:
                seq_length = 0
        
        return max_seq_length + 1

        