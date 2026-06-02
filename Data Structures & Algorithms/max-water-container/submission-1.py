class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #depends on height and width - check areas everytime we move pointers
        # area = 0
        l = 0
        r = len(heights) - 1
        maxarea = (r-l) * min(heights[r],heights[l]) #outside loop, let it be the area

        while l < r: 
            area = (r-l) * min(heights[r],heights[l])
            if heights[l] < heights[r]:
                l += 1
                if area > maxarea:
                    maxarea = area
            else:
                r -= 1
                if area > maxarea:
                    maxarea = area

        return maxarea
            