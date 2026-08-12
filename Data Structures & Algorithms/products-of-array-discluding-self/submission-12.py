class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        output = []
        prefix = 1
        # instead of storing the accummulation from front and accumulation from back in separate arrays,
        # then finding their scalar product to determine output, we accummulate from front first, append to the output array,
        # then we accumulate from back and at each step, do the multiplication in-place on the output array. Hence we use half the space 
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output