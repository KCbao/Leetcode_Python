class Solution:
    def binaryGap(self, N: int) -> int:
        binaryN = bin(N)
        maxdist = 0
        startidx = str(binaryN).find('1')
        if startidx == -1:
            return 0
        else:
            for idx in range(startidx+1, len(binaryN)):
                if binaryN[idx] == '1':
                    maxdist = max(idx-startidx, maxdist)
                    startidx = idx
            return maxdist
        