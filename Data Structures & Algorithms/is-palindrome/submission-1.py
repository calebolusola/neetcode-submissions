class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        s_norm = "".join(filter(str.isalnum, s.lower()))
        end = len(s_norm)-1

        for _ in range(end):
            if s_norm[start] != s_norm[end]:
                return False
            start += 1
            end -= 1
        return True