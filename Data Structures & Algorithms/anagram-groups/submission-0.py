class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap to store
        anagrams = dict()
        
        for i in range(len(strs)):
            sorted_candidate: str = "".join(sorted(strs[i]))
            if sorted_candidate in anagrams:
                anagrams[sorted_candidate].append(i)
            else:
                anagrams[sorted_candidate] = [i]
        return self.processedAnagrams(strs, anagrams)
    
    def processedAnagrams(self, strs, anagrams_map: Dict):
        ret_list = []
        for key in anagrams_map:
            group = []
            for index in anagrams_map[key]:
                group.append(strs[index])
            ret_list.append(group)
        return ret_list
