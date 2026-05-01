class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # k: fixed size : not given
        # longest subarray with distint 2 digits


        mp = {}
        i,j =0,0
        mx = 0

        while j<len(fruits):
            mp[fruits[j]] = mp.get(fruits[j], 0) + 1

            while len(mp)>2:
                mp[fruits[i]] -= 1

                if mp[fruits[i]] == 0:
                    del mp[fruits[i]]
                
                i+=1
            
            mx = max(mx, j-i+1)
            j+=1

        return mx




        