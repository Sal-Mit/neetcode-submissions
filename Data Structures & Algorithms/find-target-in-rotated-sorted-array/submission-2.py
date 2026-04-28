class Solution:
    def search(self, nums: List[int], target: int) -> int:


        def findMin():
            start, end = 0, len(nums) - 1
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid
            return start
        
        # Step 2: Standard binary search
        def binarySearch(start, end):
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        # Find rotation point
        minIdx = findMin()
        
        # Step 3: Search both sorted subarrays
        r = binarySearch(minIdx, len(nums) - 1)  # Right sorted portion
        if r != -1:
            return r
        
        l = binarySearch(0, minIdx - 1)  # Left sorted portion
        return l

        