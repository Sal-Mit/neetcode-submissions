import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        nums = [-x for x in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            if x != y:
                y = x - y
                heapq.heappush(nums, y)

        return -(nums[0]) if nums else 0




        