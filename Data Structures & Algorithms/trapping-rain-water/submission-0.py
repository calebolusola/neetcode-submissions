class Solution:
    def trap(self, height: List[int]) -> int:
        # first observation is that if we have 2 walls surrounding a 0-height wall, then the height of
        # water it contains = the height of the shorter wall.

        # using pointers coming from the left and right,
        # as per hint #2
        # therefore, water trapped at height[i] = min(height[l], height[r]-height[i])
        # i.e, for index i to hold water, the wall to the right of i must be higher than i, and the wall
        # to the left must be of height > 0. The height of water contained would then be = the
        # min(height[l], height[r] {i'm not yet sure why we subtract height[i] from height[r] }),

        l, r = 0, len(height) - 1
        left_max = right_max = 0
        total_water_content = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    total_water_content += left_max - height[l]
                l += 1
            
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total_water_content += right_max - height[r]
                    
                r -= 1
        return total_water_content