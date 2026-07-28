class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency map created
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # finding K most frequent values
        # building key-pair list
        freq_list = []
        for key in freq_map:
            freq_list.append([freq_map[key], key])

        # sorting list
        sorted_freq_list = sorted(freq_list)
        print(sorted_freq_list)

        ret_list = []
        for i in range(k):
            ret_list.append(sorted_freq_list[len(sorted_freq_list) - i - 1][1])
        
        return ret_list

        
        