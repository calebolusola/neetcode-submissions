class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we want to flatten the matrix to an array, since we are told it's sorted row/column-wise
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, ((rows * cols) - 1)

        while left <= right:
            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            print(f"Row: {row}, Col: {col}")

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False