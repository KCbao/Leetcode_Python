# idea: build in function - replace, in-place change
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        