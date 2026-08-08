class Solution:
    @staticmethod
    def isAnagramOf(word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        hist = {}
        for char in word1:
            hist[char] = hist.get(char, 0) + 1
        for char in word2:
            if char not in hist:
                return False
            hist[char] -= 1
        return all(freq == 0 for freq in hist.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            # generate a canonical representative for each anagram group
            # (i.e a sorted string for an anagram will represent every anagram of that group)
            counts = [0] * 26

            for char in word:
                counts[ord(char) - ord("a")] += 1

            key = tuple(counts)
            groups.setdefault(key, []).append(word)
            
        return list(groups.values())
