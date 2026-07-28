class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq_dict = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0,
            'G': 0,
            'H': 0,
            'I': 0,
            'J': 0,
            'K': 0,
            'L': 0,
            'M': 0,
            'N': 0,
            'O': 0,
            'P': 0,
            'Q': 0,
            'R': 0,
            'S': 0,
            'T': 0,
            'U': 0,
            'V': 0,
            'W': 0,
            'X': 0,
            'Y': 0,
            'Z': 0,
        }
        l = 0
        r = 0
        max_window_size = 0

        for r in range(len(s)):
            char_freq_dict[s[r]] += 1
            # calculating number of replacements required
            if (r - l + 1) - max(char_freq_dict.values()) > k:
                char_freq_dict[s[l]] -= 1 # as a consequence of moving left index forward
                l += 1
            max_window_size = max(max_window_size, (r - l) + 1) # checking for max_window_size here
        
        return max_window_size