class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        lo, hi = max(nums), sum(nums)

        def can_split(limit):
            pieces = 1
            cur = 0
            for x in nums:
                if cur +x > limit:
                    pieces += 1
                    cur = x
                else:
                    cur += x
            return pieces <= k

        while lo < hi:
            mid = (lo+hi) //2
            if can_split(mid):
                hi = mid
            else:
                lo = mid +1
        return lo
    
    # print(splitArray([2, 4, 10, 1, 5], 2))

        