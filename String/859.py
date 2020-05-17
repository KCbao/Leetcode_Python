class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == B:
            if len(Counter(A)) == 1:
                return True
            for item in Counter(A).values():
                if item > 1:
                    return True
        if len(A) != len(B):
            return False
        else:
            mismatchA,mismatchB = [],[]
            for idx in range(len(A)):
                if A[idx] != B[idx]:
                    mismatchA.append(A[idx])
                    mismatchB.append(B[idx])
            if len(mismatchA) != 2 or len(mismatchB) != 2:
                return False
            if Counter(mismatchA) != Counter(mismatchB):
                return False
            return True