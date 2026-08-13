class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        longest = 0
        counter = 0

        for num in nums_set:
            if num-1 in nums_set:
                continue
            counter = 0
            current_num = num
            while current_num in nums_set:
                counter += 1
                current_num += 1
            if counter > longest:
                longest = counter
        return longest