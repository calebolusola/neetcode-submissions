class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        return "".join(reversed(s)) == s