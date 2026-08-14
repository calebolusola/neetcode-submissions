class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1, 1, 2, 4, 5] target = 7, [1, 4]
        # we walk through the nums array. for every num we encounter, check if target-num is in the array and target-num > num
        # we need to walk it bi-directionally
        start, end = 0, len(numbers)-1

        while start < end:
            # if we encounter it while walking forwards, return it.
            total = numbers[start] + numbers[end]
            if total > target:
                end -= 1
            elif total < target:
                start += 1
            else:
                return [start+1, end+1]
