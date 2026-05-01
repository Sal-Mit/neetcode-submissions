class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        #size: unknown (j-i+1)

        i,j =0,0
        temp = 0
        mn = float('inf')

        while j<len(nums):
            temp+= nums[j]
        
            while temp>=target:
                mn = min(mn, j-i+1)
                temp -= nums[i]
                i+=1

            j+=1

        return 0 if mn == float('inf') else mn



        