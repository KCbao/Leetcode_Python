# Question 303
# Idea: 
# Construct a new array of up-to-point sum, and we can query as many times as we want in the future
# Time complexity: O(n) 造新arr的时间
# Auxilary Memory: O(n) 新的arr
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lst = [0]
        for num in nums:
            self.lst.append(self.lst[-1]+num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
         return self.lst[j+1]-self.lst[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)