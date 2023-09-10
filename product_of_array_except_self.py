# METHOD:
# 1. initialize a temp value holder that traverses from the left and a temp value holder for the same to traverse from the right
# 2. assign pointers from left and right=> to keep track of the current value in the nums list and to update the values in the result list
# 3. step1. update the result[pointer_from_left]= value_from_left and result[pointer_from_right]= value_from_right
#  this way => update the current index with the mutlipliers from both sides of the current value without including the current value
# 4. step2. update the value_from_left *= nums[pointer_from_left] and value_from_right *= nums[pointer_from_right] thereby picking up the current value at the respective indexes as a multiplier for the next result index
 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            value_from_left = 1
            value_from_right = 1
            result = [1]*len(nums)
            for i in range(len(nums)):
                pointer_from_left = i
                pointer_from_right = len(nums)-1-i
                # first update the current result index
                if pointer_from_left == pointer_from_right:
                    result[pointer_from_left] = value_from_left * value_from_right
                else:
                    result[pointer_from_left] *= value_from_left
                    result[pointer_from_right] *= value_from_right

                # update the values
                value_from_left *= nums[pointer_from_left]
                value_from_right *= nums[pointer_from_right]
            return result