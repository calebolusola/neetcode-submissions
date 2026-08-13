class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        seq_lengths = []
        counter = 0

        for num in nums:
            if num-1 in nums_set:
                continue
            counter = 0
            current_num = num
            while current_num in nums_set:
                counter += 1
                current_num += 1
            seq_lengths.append(counter)

        return max(seq_lengths)