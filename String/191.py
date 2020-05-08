# idea: input n is an integer
# to change it to binary, format(n,"b")
class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(int(i) for i in str(format(n,"b")))