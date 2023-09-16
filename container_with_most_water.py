class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height)-1
        max_area = 0
        left_height = height[left_index]
        right_height = height[right_index]
        while(left_index<right_index):
            
            max_area = max(max_area,abs(left_index-right_index) * min(left_height, right_height))
            if left_height>right_height:
                right_index-=1
                right_height = height[right_index]
            elif right_height>=left_height:
                left_index+=1
                left_height = height[left_index]

        return max_area