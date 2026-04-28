class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n= len(arr)
        
        max = arr[n-1]
        arr[n-1] = -1
        for i in range(len(arr)-2,-1,-1):
            curr = arr[i]
            arr[i] = max
            if curr > max:
                max = curr

          
                

        return arr




