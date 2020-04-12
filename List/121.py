# idea1: create a fun: input num and a list, return a profit
# recursively call this fun from num, prices[num+1:]

# idea2: sort list first, get index of the sorting list in ascending order
# e.g., lst = [4,1,0], sortidx = [2,1,0]
# given an idx, 2, look in [1,0] to see if there an index greater than 2, 
# meaning a larger number exist later than lst[2], if there is, profit= lst[j]-lst[2]
# this idea exceeds time limits when encounter a long list

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx,num in enumerate(prices):
            profit = max(profit, self.Profit(prices[idx+1:], num))
        return profit
        
    def Profit(self, prices, num):
        profit = 0
        if prices != []:
            if num <= max(prices):
                profit = max(prices)-num
        return profit
         
        # idea 2:
        # sortidx = sorted(range(len(prices)), key=lambda k: prices[k])
        # profit = 0
        # for i,idx in enumerate(sortidx):
        #     for j in sortidx[:-len(sortidx)+i:-1]:
        #         # print(idx, j)
        #         if idx <= j:
        #             profit = max(profit, prices[j] - prices[idx])
        # return profit