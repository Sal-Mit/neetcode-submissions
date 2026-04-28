class Solution:
    def findMin(self, nums: List[int]) -> int:


        n = len(nums)
        start, end = 0, n-1

        if nums[start] <= nums[end]:
            return nums[start]

        while start < end:
            mid = start + (end - start) // 2
            
            # If mid element is greater than end element,
            # the minimum must be in the right half
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                # Minimum is in the left half (including mid)
                end = mid
        
        # When start == end, we've found the minimum
        return nums[start]

        