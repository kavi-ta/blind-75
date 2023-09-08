class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s =="":
            return True
        temp_str = ""
        for i in s:
            if (ord(i)<=122 and ord(i)>=97) or (ord(i)<=57 and ord(i)>=48) or  (ord(i)<=90 and ord(i)>=65):
                temp_str += i.lower()
        return temp_str == temp_str[::-1]