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
        s_norm = "".join(filter(self.isalnum, s.lower()))
        end = len(s_norm)-1

        for _ in range(end):
            if s_norm[start] != s_norm[end]:
                return False
            start += 1
            end -= 1
        return True