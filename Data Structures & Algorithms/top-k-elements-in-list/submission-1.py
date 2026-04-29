class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr= []

        for key, val in count.items():
            arr.append([val, key])

        # arr.sort(reverse = True)
        # return arr[k-1][1] 

        arr.sort() 

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])


        return res      