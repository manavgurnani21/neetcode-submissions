class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two-pointer solution (O(n) time and O(1) space)
        l = 0
        r = len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                print(f"Comparing {s[l].lower()} and {s[r].lower()}")
            l += 1
            r -= 1

        return True
        