class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            signature = "".join(sorted(word))
            groups.setdefault(signature, []).append(word)
        
        return [i for i in groups.values()]