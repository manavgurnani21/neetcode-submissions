class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return []
        output = [0] * len(nums)
        # finding list product
        nums_product_no_zeroes = nums[0]
        numZeroes = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                numZeroes += 1
                continue
            nums_product_no_zeroes *= nums[i]
        print(nums_product_no_zeroes)

        nums_product = nums_product_no_zeroes if numZeroes < 1 else 0
        print(nums_product)

        # constructing output
        for i in range(len(nums)):
            if nums[i] == 0:
                if numZeroes > 1:
                    output[i] = 0
                else:
                    output[i] = nums_product_no_zeroes
            else:
                output[i] = nums_product // nums[i]

        print(output)

        return output