class Solution:
    @staticmethod
    def isalnum(c: str):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
            )
    def isPalindrome(self, s: str) -> bool:
        start = 0
        # s_norm = "".join(filter(self.isalnum, s.lower()))
        end = len(s)-1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True