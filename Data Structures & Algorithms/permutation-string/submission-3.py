class Solution:
    def checkInclusion(self, s1, s2):
        window_size = len(s1)
        if window_size > len(s2):
            return False
        s1_ord = sorted(s1)
        for i in range(len(s2)-window_size+1):
            if sorted(s2[i:i+window_size]) == s1_ord:
                return True
        return False