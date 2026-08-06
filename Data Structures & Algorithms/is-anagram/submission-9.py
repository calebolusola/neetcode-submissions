class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram
        # nagaram

        hash_map_s = {}
        hash_map_t = {}

        # Checks:
        # 1. they must have the same length
        if len(s) != len(t):
            return False

        # 2. they must have the exact same word histogram
        for char in s:
            if char not in hash_map_s:
                hash_map_s[char] = 0
            hash_map_s[char] += 1

        for char in t:
            if char not in hash_map_t:
                hash_map_t[char] = 0
            hash_map_t[char] += 1
        if hash_map_s != hash_map_t:
            return False
        return True