class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == "":
            if B == "":
                return True
            else:
                return False
        for idx in range(len(A)):
            newstr = A[idx+1:]+A[:idx+1]
            if B == newstr:
                return True
        return False
        