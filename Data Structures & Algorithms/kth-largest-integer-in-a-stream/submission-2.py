import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minheap = nums
        self.k = k        
        # create a min heap
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
       

    def add(self, val: int) -> int:
        # adds value to heap
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]






        
