class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []

        # make frequency hashmap from list of numbers
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        print(freq_map)
        
        # take hashmap and make bucket list of numbers
        count_list = [[]] * (len(nums) + 1)
        for key in freq_map:
            print(f"Adding value {key} to count index of {freq_map[key]}")
            count_list[freq_map[key]] = count_list[freq_map[key]] + [key]
            print(count_list)
        print(count_list)

        # pick top k frequencies until desired number achieved
        ret_list = []
        for i in range(len(count_list) - 1, -1, -1):
            if len(ret_list) == k:
                return ret_list
            if count_list[i] != []:
                ret_list.extend(count_list[i])
        
        return ret_list