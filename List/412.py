class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 != 0:
                ans += ['Fizz']
            elif i%5 == 0 and i%3 != 0:
                ans += ['Buzz']
            elif i%15 == 0:
                ans += ['FizzBuzz']
            else:
                ans += [str(i)]
        return ans