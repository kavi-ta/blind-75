class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        # implementing stack check
        empty_str = []
        brackets = {"(": ")", "{":"}", "[":"]"}
        for i in s:
            if i in brackets.keys():
                # i represents one of the opening brackets=> add to stack
                empty_str.append(i)
            else:
                # i represents one of the closing brackets
                if len(empty_str)==0:
                    # if stack is empty=> no corresponding opening bracket present
                    return False
                # stack not empty=> check for opening bracket in the stack's last element
                elif brackets[empty_str[-1]] == i:
                    # if last bracket in the stack is the opening bracket of i=> pop the stack
                    empty_str.pop()
                else:
                    # last bracket in the stack is not the opening bracket
                    return False
        return len(empty_str)==0

s = "()[]{}"
solution = Solution()
result = solution.isValid(s)
print(result)