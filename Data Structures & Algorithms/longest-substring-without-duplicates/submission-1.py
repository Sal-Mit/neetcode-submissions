class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i,j = 0,0

        l = {}
        result = 0

        while j<len(s):
            l[s[j]] = l.get(s[j],0) + 1

            while (l[s[j]] > 1):
            # we can also compare hasmap.size with total count of values
                l[s[i]] = l.get(s[i],0) - 1
                if l.get(s[i]) == 0:
                    del l[s[i]]
                i+=1
            
            result= max(result, j-i+1)
            j+=1

        return result



        