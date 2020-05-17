class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair = 1
        sumcoins = 0
        remain = n-sumcoins
        while sumcoins + stair <= n:
            sumcoins += stair
            remain = n-sumcoins
            stair += 1
        if stair == remain: 
            return stair
        else:
            return stair-1