class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:



        low, high = 1,max(piles)
        ans = max(piles) 
        

        while low <= high:

            mid = low + (high-low)//2

            hours=0

            for pile in piles:
                hours += math.ceil(pile/mid)

            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

            

        return ans



        