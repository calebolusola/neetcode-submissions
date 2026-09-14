class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # if there is a smaller number to the right, slide right
            # if there is a smaller number to the left, slide left
            if nums[mid] > nums[right]:
                left =  mid + 1
            else:
                right = mid

        
        return nums[left]
