# idea: if n>=4, sqrt(n)<n//2
# use start, mid, end where mid=midpoint b/t start and end points
# divide and conquer, to see num lies in between start, mid, or mid, end, then update accordingly
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1 or num == 4:
            return True
        else:
            start = 3
            end = num//2
            while start**2<= num <= end**2:
                if start**2== num or num== end**2:
                    return True
                mid = start+(end-start)//2
                if mid**2<= num <= end**2:
                    if mid**2== num or num== end**2:
                        return True
                    start = mid
                elif start**2<= num<= mid**2:
                    if start**2== num or num== mid**2:
                        return True
                    end = mid              
                if end-start == 1:
                    return False
            return False