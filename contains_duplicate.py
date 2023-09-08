class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = {}
        for i in nums:
            if i not in count.keys():
                count[i] = 0
            else:
                count[i]+=1
                return True
        return False

nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)