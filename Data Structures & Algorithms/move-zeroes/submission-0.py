class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        #one pointer will keep track position, and one for the element

        stanby, moving = 0, 0

        for moving in range(len(nums)):

            if nums[moving] != 0:
                nums[stanby], nums[moving] = nums[moving], nums[stanby]
                stanby += 1
        
        return nums

        
  





        