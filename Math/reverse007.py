# Given an 32-bit int, output an int of reverse order, must be 32-bit
# Idea:
# 32-bit signed int: [-2^31 : 2^31-1] : ^31 因为他是signed int， -1 因为有0
# 从右往左，个位十位, be aware of overflow
# Time : O(n)
# Space : O(n+1) == O(n)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # initialize num
        num = 0
        sign = lambda x: (x>=0)-(x<0)
        sig = sign(x)
        x = abs(x)
        while x != 0:
            # get digit by mod: mod(a,b) = reminder a/b
            temp = x % 10 
            # num是最后output value
            num =  num * 10 + temp
            # update x a//b: quotient
            x = x // 10 

        # check if it's overflow
        if -2**31 <= sig*num <= 2**31-1:
            return sig*num
        else: 
            return 0

x = 123
x = -123
sol = Solution()
print(sol.reverse(x))