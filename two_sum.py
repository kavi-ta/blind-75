def twoSum(nums , target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
nums = [2,7,11,15]
target = 9
result = twoSum(nums, target)
print(result)