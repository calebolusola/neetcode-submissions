class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [3, 2, 1, 4, 5] target = 7, [1, 4]
        # we walk through the nums array. for every num we encounter, check if target-num is in the array and target-num > num
        # we need to walk it bi-directionally
        num_length = len(numbers)
        start, end = 0, num_length-1
        num_set = set(numbers)

        while start < end:
            # if we encounter it while walking forwards, return it.
            diff_start = target-numbers[start]
            if diff_start in num_set:
                diff_start_pos = numbers.index(diff_start) if numbers[start] != diff_start else numbers.index(diff_start, start + 1)
                if diff_start_pos > start:
                    return [start+1, diff_start_pos+1]

            # if we encounter it while walking backwards, return it.
            diff_end = target-numbers[end]
            if diff_end in num_set:
                diff_end_pos = numbers.index(diff_end) if numbers[end] != diff_end else numbers.index(diff_end, end - 1)
                if end > diff_end_pos:
                    print("that hit")
                    return [diff_end_pos+1, end+1]
            
            start += 1
            end -= 1

        return [0, 0]