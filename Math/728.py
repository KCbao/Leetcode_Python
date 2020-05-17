class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right+1):
            flag = True
            idx = 0
            strnum = str(num)
            if strnum.find('0') != -1:
                flag = False
            while idx<len(strnum) and flag == True:
                digit = int(strnum[idx])
                if num%digit != 0:
                    flag = False
                if idx == len(strnum)-1 and flag == True:
                    ans.append(num)
                idx += 1
            num += 1
        return ans