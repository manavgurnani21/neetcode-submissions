class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums to a set
        set_nums = set(nums)
        longest_sequence = 0
        # traverse set to find all possible consecutive lists
        for num in set_nums:
            if num - 1 not in set_nums:
                sequence_length = 1 # counting first element of sequence
                # when new sequence found, keep traversing to find consecutives
                while (num + sequence_length) in set_nums:
                    sequence_length += 1
                longest_sequence = max(sequence_length, longest_sequence)
        return longest_sequence