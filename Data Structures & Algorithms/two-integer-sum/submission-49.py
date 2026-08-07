class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [4,5,6]
        # target -> 10
        # initialize an empty dict
        encountered = {}
        # iterate through the numbers, check if the [target - num] a.k.a the diff exists in the dict
        # if it exists, return its the index of the num and the index of the diff's location 
        # else add the num to the dict with it's index as it's value
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in encountered:
                return [encountered[diff], idx]

            encountered[num] = idx
        return [0]
