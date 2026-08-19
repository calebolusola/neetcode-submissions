class Solution:
    def isValid(self, s: str) -> bool:
        # s = "([{}])"
        # if there is a parenthesis at i, there must be the same one at len(s)-if
        stack = []
        openings = {"{", "(", "["}
        closings = {"}", ")", "]"}

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in openings:
                stack.append(char)
            elif char in closings:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                continue

        if len(stack) > 0:
            return False
        return True