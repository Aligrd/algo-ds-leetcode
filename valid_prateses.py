# return true if every open paranthes have corresponding closing or false if not
# masale leetcode


def validParentheses(s: str):
    stack = []
    lookup = {"}": "{", "]": "[", ")": "("}
    for p in s:
        if p in lookup.values():
            stack.append(p)
        elif stack and lookup[p] == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack


# test
judge1 = "[]{}()"
judge2 = "[]{()}"
judge3 = "[{()}]"


print(validParentheses(judge1))
print(validParentheses(judge2))
print(validParentheses(judge3))
