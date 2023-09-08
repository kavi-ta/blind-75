class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert x to str
        return str(x)==str(x)[::-1]