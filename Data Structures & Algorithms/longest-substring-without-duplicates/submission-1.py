class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0 # the maximum length of any substring
        l = 0 # the left pointer
        seen = {} # the hastable used to track all seen characters
        for r in range(len(s)):
            curr_char = s[r] # current char pointed to by right
            if curr_char in seen and seen[curr_char] >= l: # if we have stumbled upon a duplicate and if that character is right of the left pointer
                l = seen[curr_char] + 1 # shift left by 1 to remove duplicate character
            else:
                maxlen = max(maxlen, r - l + 1) # means its a new unique substring so capture length
            seen[curr_char] = r # update most recent spotting of character
        return maxlen 