## idea: 1*x+2*y = n, x,y is int
# if x,y!=0, need combination, say 1+2+1, 1+1+2, 2+1+1, total is (x+y)!/(x!y!)
# determine if a float is int, use .is_integer()
# determine if a int is int, use isinstance(x,int)
class Solution:
    def climbStairs(self, n: int) -> int:
        num = 0
        for x in range(n+1):
            if ((n-x)/2).is_integer():
                y = (n-x)/2
                if x>0 and y>0:
                    num += int(math.factorial(x+y)/(math.factorial(x)*math.factorial(y)))
                else:
                    num += 1
        return num
       
        