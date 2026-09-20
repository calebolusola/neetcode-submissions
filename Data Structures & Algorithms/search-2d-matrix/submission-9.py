class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we want to flatten the matrix to an array, since we are told it's sorted row/column-wise
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, (rows * cols) - 1

        while start <= end:
            mid = (start + end) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False