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
        # go through the strs array, build a histogram for each char.
        # then, group the histograms together to build the output array.

        # if len(set(strs)) == 1:
        #     return [strs]

        # initialize empty array
        groups = {}

        # for every unique element we encounter, add it to the array, for example:
        # strs = ["act","pots","tops","cat","stop","hat"]
        # {"act": ["act"], "pots": ["pots"], ... }

        
        for word in strs:
            key = "".join(sorted(word))
            groups.setdefault(key, []).append(word)
            
        return list(groups.values())
