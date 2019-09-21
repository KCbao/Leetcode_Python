# Idea: similar to 007 except no overflow
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = 0
        sign = lambda x: (x>=0)-(x<0)
        sig = sign(x)
        a = x
        if sig == -1 :
            return False
        else:
            while x != 0:
                # get digit % - mod(a,b): remainder
                temp = x % 10
                # update num
                num = num * 10 + temp
                # update x a//b: quotient
                x = x//10
            if a == num:
                return True
            else: 
                return False

# x = 121
# x = -123
x = 10
sol = Solution()
print(sol.isPalindrome(x))