class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create list of all possible characters
        # create hashmap for all possible anagrams
            # key: set of alphabet frequencies (key lookup is O(1) due to hashing)
            # value: list of all anagrams
        # return list of lists
        ret_list = defaultdict(list)
        for s in strs:
            count = [0] * 26 # frequency list
            for c in s:
                count[ord(c) - ord('a')] += 1 # updating frequecy
            ret_list[tuple(count)].append(s) # adding tuple of list as key for hashing
        return list(ret_list.values())
