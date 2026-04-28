class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashset_count = {}

        for i in s:
            hashset_count[i] = hashset_count.get(i,0) + 1

        for i in t:
            if i not in hashset_count:
                return False
            hashset_count[i] -= 1
            if hashset_count[i]<0:
                return False
        
        return True

        

            


        