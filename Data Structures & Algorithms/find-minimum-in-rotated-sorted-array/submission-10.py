class Solution:
    def findMin(self, nums: List[int]) -> int:


        n = len(nums)
        start, end = 0, n-1

        if nums[start] <= nums[end]:
            return nums[start]

        while start < end:
            mid = start + (end - start) // 2

            prev = (mid -1 +n)%n
            nextt = (mid+1)%n

            if (nums[mid] <= nums[nextt]) and (nums[mid] <= nums[prev]):
                return nums[mid]
            
            # If mid element is greater than end element,
            # the minimum must be in the right half
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                # Minimum is in the left half (including mid)
                end = mid
        
        # When start == end, we've found the minimum
        return nums[start]

        