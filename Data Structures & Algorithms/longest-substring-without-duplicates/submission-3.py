class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #the letter shouldnt be in the temp we are creating while iterating through the loop

        i=0
        temp = {}
        max_count = 0

        for j in range(len(s)):

            if s[j] in temp and temp[s[j]] >= i:
                i=temp[s[j]] +1

            temp[s[j]] = j
            max_count = max(max_count, j-i+1)

        return max_count


            





        