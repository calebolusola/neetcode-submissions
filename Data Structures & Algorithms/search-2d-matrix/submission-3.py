class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the key is to treat the matrix like one big array by flattening it
        nums = []
        for row in matrix:
            nums.extend(row)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False