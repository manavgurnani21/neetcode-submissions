from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_hash_table = defaultdict(int)
        # one pass through s (add to hashtable)
        for character in s:
            string_hash_table[character] += 1

        # one pass through t (subtract from hashtable)
        for character in t:
            string_hash_table[character] -= 1

        # return true if the string_hash_table is full of zeroes
        for key in string_hash_table:
            if string_hash_table[key] != 0:
                return False
        
        return True