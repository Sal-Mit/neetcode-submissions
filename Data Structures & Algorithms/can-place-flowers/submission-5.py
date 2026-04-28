class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbednew = [0] + flowerbed + [0]

        for i in range(1,len(flowerbednew)-1):
            if flowerbednew[i-1] == 0 and flowerbednew[i] ==0 and flowerbednew[i+1] == 0 :
                flowerbednew[i] = 1
                n -= 1

        return n<=0


 


        