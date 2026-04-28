class Solution:
    def maxArea(self, heights: List[int]) -> int:


        i,j = 0, len(heights)-1
        area = 0

        while i<j:

            if (heights[i] < heights[j]):
                area = max(area,heights[i]*(j-i))
                i+=1

            elif (heights[i] > heights[j]):
                area = max(area,heights[j]*(j-i))
                j-=1

            else:
                area = max(area,heights[j]*(j-i))
                i+=1
                j-=1

        return area

        