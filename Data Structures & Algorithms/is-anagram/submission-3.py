class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # "bbcc"
        # "ccbc"
        # count how many times the unique letters in a appear in a versus in b
        
        if set(s) == set(t) and len(s) == len(t) and sum(ord(i) for i in s) == sum(ord(j) for j in t):
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
                return True
            return True
        else:
            return False