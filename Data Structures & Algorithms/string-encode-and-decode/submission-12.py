class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["hello", "world"]
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += f"{length}#{word}"
        return encoded
        
    def decode(self, s: str) -> List[str]:
        # 5#hello5#world
        decoded = []
        current_index = 0
        
        while current_index < len(s):
            # search for the first occurence of "#" starting from current index
            delimiter = s.index("#", current_index)
            length = int(s[current_index:delimiter])
            
            start = delimiter + 1
            end = start + length
            
            decoded.append(s[start: end])
            current_index = end
        return decoded