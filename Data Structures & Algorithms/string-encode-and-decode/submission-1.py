class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string: str = ""
        for s in strs:
            encoded_string += str(s + "±")
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list: List[str] = []
        start = 0
        end = 0
        while end < len(s):
            if s[end] == "±":
                decoded_list.append(s[start:end])
                start = end + 1 if end < len(s) else end
                end = start
            else:
                end += 1
        return decoded_list