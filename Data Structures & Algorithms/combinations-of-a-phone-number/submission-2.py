class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r", "s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y", "z"]
        }

        combinations = []

        if digits == "":
            return []

        def callback(nums, call_str):
            if len(nums) == 0:
                combinations.append(call_str)
            else:
                curr_num = nums[0]
                nums = nums[1:]
                for alpha in mapping[curr_num]:
                    # print(f"callback({nums}, {call_str + alpha})")
                    callback(nums, call_str + alpha)
        
        callback(list(digits), "")

        return combinations