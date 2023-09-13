class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = current_sum = nums[0]
        i = 1
        n = len(nums)
        while(i<n):
            current_sum = max( current_sum+nums[i] , nums[i])
            max_val = max(current_sum, max_val)
            i+=1
        return max_val