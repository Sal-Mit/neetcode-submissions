class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i,j = 0,0
        mp = {}
        mx = 0



        while j<len(s):
            mp[s[j]] = mp.get(s[j], 0) + 1

            while mp[s[j]] > 1: 
                mp[s[i]] -= 1 
                i+=1

            mx = max(mx,j-i+1)
            j+=1

        return mx

        