# idea: ^: XOR
# idea: bin(x^y) will first get same length binary
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(int(i) for i in bin(x^y)[2:])