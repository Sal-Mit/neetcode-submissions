from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = Counter(nums)

        bucket = [[] for _ in range (len(nums)+1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        result =[]
        for i in range (len(bucket)-1,-1,-1):
            if bucket[i]:
                result.extend(bucket[i])
                if len(result)>k:
                    break

        return result[:k]


        