class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the key is to turn 3 sum into 2 sum II
        # i + j + k = 0; i  = - (j + k)
        # we freeze i on each iteration, then do the slide walk from both sides with -i as the target, then we advance i by one
        nums.sort()
        found = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i+1, len(nums) - 1
            target = -nums[i]
            while left < right:
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    found.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return found