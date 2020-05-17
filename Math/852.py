class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = 0
        for idx, item in enumerate(A):
            if item > peak:
                peak = item
            elif item < peak:
                return idx-1