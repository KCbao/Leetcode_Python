class Solution:
    def titleToNumber(self, s: str) -> int:
        colnum = 0
        for i in range(-1, -len(s)-1, -1):
            colnum += (ord(s[i])-64)*26**(-i-1)
        return colnum
        