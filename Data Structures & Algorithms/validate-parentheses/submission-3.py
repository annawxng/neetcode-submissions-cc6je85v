class Solution:
    # stack
    def isValid(self, s: str) -> bool:
        stack = []
        for chr in s:
            if chr == '(' or chr == '{' or chr == '[':
                stack.append(chr)
            elif chr == ')' or chr == '}' or chr == ']':
                if stack:
                    top = stack.pop()
                    if (chr == ')' and top != '(') or (chr == '}' and top != '{') or (chr == ']' and top != '['):
                         return False
                else:
                    return False
        if stack:
            return False
        return True
                