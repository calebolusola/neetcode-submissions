class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 2, 3]
            # [3, 2, 3]
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and i !=j:
                    return [i, j]