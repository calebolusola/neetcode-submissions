class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the key is to turn 3 sum into 2 sum II
        # i + j + k = 0; i  = - (j + k)
        # we freeze i on each iteration, then do the slide walk from both sides with -i as the target, then we advance i by one
        nums.sort()
        found = []
        for i in range(len(nums)):
            # don't freeze the same value twice to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            target = -nums[i] # -i = (j + k)
            while left < right:
                # perform the bi-directional walk starting from i + 1
                # (i.e starting from the front of the frozen value)
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    found.append([nums[i], nums[left], nums[right]])
                    # we used these left/right values in a valid triplet,
                    # so move both pointers to search for another pair.
                    left += 1
                    right -= 1

                    # skip repeated values so we don't generate the same triplet again.
                    # we check the next value after the current and continue skipping to the next value
                    # until we find a value that's unique from the previous one for both the l & r pointers.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return found