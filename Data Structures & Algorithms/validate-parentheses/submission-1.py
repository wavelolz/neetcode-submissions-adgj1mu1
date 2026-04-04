class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {")":"(", "}":"{", "]":"["}
        for i in range(len(s)):
            if s[i] in pair.values():
                stack.append(s[i])
            
            if s[i] in pair.keys():
                if len(stack)>0:
                    if pair[s[i]] == stack[-1]:
                        stack = stack[:-1]
                    else:
                        return False
                else:
                    return False
        return True if len(stack)==0 else False

        