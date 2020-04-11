class Solution:
    def titleToNumber(self, s: str) -> int:
        colnum = 0
        for idx, item in enumerate(s)[::-1]:
            colnum += (ord(s[i])-64)*26**(-i-1)
        return colnum
        