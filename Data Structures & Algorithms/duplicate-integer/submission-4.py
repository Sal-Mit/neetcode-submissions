class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # hashset = set(nums)
        # if len(nums) == len(hashset):
        #     return False
        # else:
        #     return True

        #More FAANG approach code
        
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        