class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_sorted = sorted(nums)

        counter = 1
        longest = 1

        for idx in range(1, len(nums_sorted)):
            diff = nums_sorted[idx] - nums_sorted[idx - 1]

            if diff == 1:
                counter += 1
                longest = max(longest, counter)

            elif diff == 0:
                continue

            else:
                counter = 1

        return longest