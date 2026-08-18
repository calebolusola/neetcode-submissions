class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["hello", "world"]
        # 5#hello5#world
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        curr_idx = 0
        words = []

        while curr_idx < len(s): 
            delimiter = s.index("#", curr_idx)
            length = int(s[curr_idx: delimiter])

            start = delimiter + 1
            end = start + length

            found = s[start: end]
            words.append(found)

            curr_idx = end

        return words