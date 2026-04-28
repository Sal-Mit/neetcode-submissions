class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap_diff = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap_diff:
                return [hashmap_diff[diff],i]   

            hashmap_diff[num]=i 
            

        

        