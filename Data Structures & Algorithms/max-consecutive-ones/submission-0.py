class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currstreak = 0
        beststreak = 0
        for num in nums:
          if num == 0:
            currstreak = 0
          else:
            currstreak += 1
          if currstreak >= beststreak:
            beststreak = currstreak
        return beststreak