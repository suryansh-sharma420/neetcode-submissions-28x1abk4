class Solution:
    def isValid(self, s: str) -> bool:
        #using a stack - see an open bracket - put in stack, if close in stack, pop
        mapping = {']':'[','}':'{',')':'('}
        stack = []
        for brackets in s:
            if brackets in mapping:
                if stack and stack[-1] == mapping[brackets]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brackets)
        return True if not stack else False
