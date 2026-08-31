class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        max_substr_length = 0

        l = 0
        for r in range(len(s)):
            if s[r] in seen and l <= seen[s[r]]:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            max_substr_length = max(max_substr_length, r - l + 1)

        return max_substr_length
