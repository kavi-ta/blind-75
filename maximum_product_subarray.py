class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 1
        max_product = nums[0]
        n = len(nums)
        for i in range(len(nums)):
            if prefix == 0 : prefix = 1
            if suffix == 0 : suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[n-1-i]

            max_product = max( max_product, prefix, suffix)
        return max_product