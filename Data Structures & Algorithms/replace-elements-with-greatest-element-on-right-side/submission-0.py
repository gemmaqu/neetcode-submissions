class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        runningmax = arr[-1] # start from the orginal value of the last ele
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            curr = arr[i]
            arr[i]= runningmax
            runningmax = max(curr, runningmax)
        return arr
        