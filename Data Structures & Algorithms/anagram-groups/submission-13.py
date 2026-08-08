class Solution:
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
