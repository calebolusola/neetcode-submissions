class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashes = set()
        for n in nums:
            if n in hashes:
                return True
            hashes.add(n)
        return False
        