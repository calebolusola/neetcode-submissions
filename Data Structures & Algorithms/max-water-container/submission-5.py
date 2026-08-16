class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # they're basically asking, from this array of numbers, find 2 numbers such
        # that the difference between their indices * the minimum of their values is the highest
        i, j = 0, len(heights)-1
        max_area = 0

        while i < j:
            # area (i, j) = (j-i) * min(heights[i], heights[j])
            area = min(heights[i], heights[j]) * (j-i)
            max_area = max(max_area, area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area