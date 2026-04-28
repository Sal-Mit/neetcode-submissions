class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        a = set(nums)
        print(len(a))

        if len(nums) == len(a):
            return False
        else:
            return True
        