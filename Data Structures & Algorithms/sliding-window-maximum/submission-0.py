class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        i, j = 0, 0
        l = []
        result = []

        while j < len(nums):
            l.append(nums[j])

            if (j-i+1) < k:
                j+=1
            elif (j-i+1) == k:
                result.append(max(l))
                l.pop(0)
                j+=1
                i+=1
            else:
                i+=1

        return result
                
                




        