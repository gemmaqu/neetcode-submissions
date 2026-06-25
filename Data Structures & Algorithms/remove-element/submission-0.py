class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        for num in nums:
            if num != val: 
                nums[k] = num
                k += 1     
        return k
                