import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest_heap = []
        for i in range(len(nums)):
            if len(largest_heap) < k:
                heapq.heappush(largest_heap, nums[i])
            else:
                # need to replace
                if nums[i] > largest_heap[0]:
                    heapq.heappop(largest_heap)
                    heapq.heappush(largest_heap, nums[i])
        
        return largest_heap[0]