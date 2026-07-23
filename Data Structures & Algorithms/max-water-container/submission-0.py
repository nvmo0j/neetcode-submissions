class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water_max = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            water_max = max(water_max, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return water_max
        