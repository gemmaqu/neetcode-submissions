class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)

        return heap[0]

        # while len(nums) > 1:
        #     return -nums[index-len(nums)]