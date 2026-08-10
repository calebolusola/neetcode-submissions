class Solution:

    def encode(self, strs: List[str]) -> str:
        print("".split("0x"))
        if len(strs) == 0:
            return "\n"
        if len(strs) == 1 and not strs[0]:
            return "\n\n"
        return "0x".join(strs) if strs else "0x0x0x"
    def decode(self, s: str) -> List[str]:
        if s == "\n":
            return []
        if s == "\n\n":
            return [""]
        return s.split("0x") if s else []