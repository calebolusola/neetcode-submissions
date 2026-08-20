class Solution:
    def isValid(self, s: str) -> bool:
        openings = {"{", "[", "("}
        pairings = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for char in s:
            if char in openings:
                stack.append(char)
            elif char in pairings:
                # we must not start with a closing parenthesis
                if not stack \
                 or stack[-1] != pairings[char]: # the last opening must correspond to the first closing
                    return False
                stack.pop()

        return not stack